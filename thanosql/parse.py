import re
from types import ModuleType


def is_url(s):
    p = re.compile(r"^\s*\w*://\w*")
    if p.match(s):
        return True
    else:
        return False


def is_api_token(s):
    p = re.compile(r"^\s*API_TOKEN=\w*")
    if p.match(s):
        return True
    else:
        return False


def remove_df_from_query(s):
    # regex below searches and removes df(json, orient="records") from the query string
    # regex detects "[{df_data}]" or '[{df_data}]'
    removed_df_s = re.sub('''('|")\[[^']*\]('|")''', "", s)
    return removed_df_s


def is_multiple_queries(s):
    removed_df_s = remove_df_from_query(s)
    return ";" in removed_df_s
