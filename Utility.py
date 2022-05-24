def dict_list_should_contain_value(dicts, key, value):
    for dict in dicts:
        if str(dict[key]) == value:
            return
    raise Exception(f"'{dicts}' does not contain key '{key}' with value '{value}'")

def dict_list_should_not_contain_value(dicts, key, value):
    for dict in dicts:
        if str(dict[key]) == value:
            raise Exception(f"'{dicts}' contains key '{key}' with value '{value}'")
    return

def dict_list_should_not_contain_duplicates(dicts, key):
    found_values = []
    for dict in dicts:
        value = dict[key]
        if value in found_values:
            raise Exception(f"'{dicts}' contains duplicates for key '{key}' with value '{value}'")
        else:
            found_values.append(value)
    return
