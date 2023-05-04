import re
from types import ModuleType


def is_url(s):
    p = re.compile(r"^\s*\w*://\w*")
    return bool(p.match(s))


def is_api_token(s):
    p = re.compile(r"^\s*API_TOKEN=\w*")
    return bool(p.match(s))


def is_multiple_queries(query_string):
    # regex below finds substring that starts with '[ or "[ and ends with ]' or ]" 
    # It removes all the substrings containing semicolon which does not need to be checked.
    processed_query_string = re.sub('''('|")\[[^']*\]('|")''', "", query_string)
    return ";" in processed_query_string

def is_db_user(s):
    p = re.compile(r"\s*DB_USER=\w")
    return bool(p.match(s))

def is_db_password(s):
    p = re.compile(r"\s*DB_PASSWORD=\w")
    return bool(p.match(s))