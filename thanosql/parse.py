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


def is_multiple_queries(s):
    return ";" in s
