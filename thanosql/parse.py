from types import ModuleType
import re

def convert_local_ns(query_string, local_ns) -> str:    
    # remove local_ns items with ModuleType
    local_ns = {key:val for key, val in local_ns.items() if not isinstance(val, ModuleType)}
    
    # variables need to be converted
    var_list = list(set(map(str.strip, re.findall(r'=( *?\w+)', query_string))))
    
    # modifying query_string
    for i in range(len(var_list)):
        var = local_ns.get(var_list[i])
        if var:
            query_string = query_string.replace(var_list[i],str(var))

    return query_string