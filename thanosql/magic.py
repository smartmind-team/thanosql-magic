from IPython.core.magic import (
    Magics,
    magics_class,
    line_cell_magic,
    needs_local_scope,
)

import requests
import pandas as pd
import json

from thanosql.parse import convert_local_ns

@magics_class
class ThanosMagic(Magics):
    @needs_local_scope
    @line_cell_magic
    def thanosql(self, line=None, cell=None, local_ns={}):
        if line:
            cell = line

        if not cell:
            return
    
        query_string = convert_local_ns(cell, local_ns)
        print(query_string)
        
        data = {
            'query_string': query_string
        }
        
        res = requests.post('http://localhost:8000/api/v1/query', data=json.dumps(data))
   
        if res.status_code == 200:
            data = res.json()
            query_result = data.get('final_result')

            if query_result:
                df = pd.read_json(query_result, orient='columns')
                return df

            return
        
        else
            return res

# In order to actually use these magics, you must register them with a
# running IPython.
def load_ipython_extension(ipython):
    """Load the extension in IPython."""
    ipython.register_magics(ThanosMagic)