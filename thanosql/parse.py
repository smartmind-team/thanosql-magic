import re
import pandas as pd
from types import ModuleType


def convert_local_ns(query_string, local_ns) -> str:
    # remove local_ns items with ModuleType
    local_ns = {
        key: val for key, val in local_ns.items() if not isinstance(val, ModuleType)
    }

    # find variables need to be converted
    regex1 = '=( *?\w+)' # regex to find variables coming after "="
    regex2 = 'FROM( *?\w+)' # regex to find variables coming after "FROM"
    var_list = list(set(''.join(res).strip(' ') for res in re.findall(f'{regex1}|{regex2}', query_string)))

    # modifying query_string
    for var in var_list:
        if var in local_ns:
            local_var = local_ns[var]
            
            if isinstance(local_var, pd.DataFrame):
                local_var = local_var.to_json(orient="records", force_ascii=False)
            
            query_string = query_string.replace(var, f"'{str(local_var)}'")
        
        return query_string


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


def is_multiple_queries(s):
    return ";" in s


# deprecated.
def split_string_to_query_list(s: str) -> list:
    """
    Split semi-colon containing string to query list and exclude empty string('').
    """
    return list(filter(None, map(lambda x: x.strip(), s.split(";"))))
