import json
import os

import pandas as pd
import requests
import websocket
from IPython.core.magic import Magics, line_cell_magic, magics_class, needs_local_scope

from thanosql.exceptions import (
    ThanoSQLConnectionError,
    ThanoSQLInternalError,
    ThanoSQLSyntaxError,
)
from thanosql.parse import *
from thanosql.spinner import Spinner
from thanosql.utils import format_result

DEFAULT_API_URL = "wss://engine.thanosql.ai/ws/v1/query"


@magics_class
class ThanosMagic(Magics):
    @needs_local_scope
    @line_cell_magic
    def thanosql(self, line: str = None, cell: str = None, local_ns={}):
        if line:
            if is_url(line):
                # Set API URL
                api_url = line.strip()
                os.environ["API_URL"] = api_url
                print(f"API URL is changed to {api_url}")
                return

            elif is_api_token(line):
                # Set API Token
                api_token = line.strip().split("API_TOKEN=")[-1]
                os.environ["API_TOKEN"] = api_token
                print(f"API Token is set as '{api_token}'")
                return

            # 'line' will be treated the same as 'cell'
            else:
                cell = line

        if not cell:
            return

        api_url = os.getenv("API_URL", DEFAULT_API_URL)
        api_token = os.getenv("API_TOKEN", None)

        if not api_token:
            raise ThanoSQLConnectionError(
                "An API Token is requierd. Set the API Token by running the following: %thanosql API_TOKEN=<API_TOKEN>"
            )

        query_string = cell
        if is_multiple_queries(query_string):
            raise ThanoSQLSyntaxError("Multiple Queries are not supported.")

        if query_string:
            query_string = convert_local_ns(query_string, local_ns)

            data = {"query_string": query_string}

            try:
                ws = websocket.WebSocket()
                ws.connect(f"{api_url}?api_token={api_token}")

                ws.send(query_string)
            except:
                raise ThanoSQLConnectionError("Could not connect to the Websocket")
                ws.close()

            connection_open = True
            try:
                while connection_open:
                    output = ws.recv()
                    output_dict = json.loads(output)
                    if output_dict["output_type"] == "ERROR":
                        raise ThanoSQLInternalError(output_dict["output_message"])
                    elif output_dict["output_type"] == "CONNECTION_CLOSE":
                        break
                    elif output_dict["output_type"] == "PING":
                        continue
                    elif output_dict["output_type"] == "RESULT":
                        return format_result(output_dict)
                    else:
                        print(output_dict["output_message"])
            except KeyboardInterrupt:
                ws.close()
                raise Exception("KEYBOARD INTERRUPTION, TASK KILLED")

        return


# In order to actually use these magics, you must register them with a
# running IPython.
def load_ipython_extension(ipython):
    """Load the extension in IPython."""
    ipython.register_magics(ThanosMagic)
