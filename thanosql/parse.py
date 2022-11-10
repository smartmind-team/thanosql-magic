import re
import pandas as pd
from types import ModuleType


def convert_local_ns(query_string, local_ns) -> str:
    # remove local_ns items with ModuleType
    local_ns = {
        key: val for key, val in local_ns.items() if not isinstance(val, ModuleType)
    }

    # find variables need to be converted
    # below codes find all the variables come after "=" and "FROM"
    regex = '(=|FROM)( *?\w+)'
    var_list = list(set(t[1].strip(' ') for t in re.findall(regex, query_string)))

    # modifying query_string
    for i in range(len(var_list)):
        var = local_ns.get(var_list[i])
        if var is not None:
            if isinstance(var, pd.DataFrame):
                var = var.to_json(orient="records", force_ascii=False)

            query_string = query_string.replace(var_list[i], f"'{str(var)}'")

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
