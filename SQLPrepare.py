def where_and(conditions):
    if not isinstance(conditions, list):
        raise Exception('Argument given to SQLPrepare.where_and is not a list.')
    if len(conditions) == 0:
        return ''
    where_clause = 'WHERE '
    for i, condition in enumerate(conditions):
        where_clause += condition
        if not i + 1 == len(conditions):
            where_clause += ' AND'
            where_clause += '\n'
    return where_clause

def comma_seperate(items):
    if not isinstance(items, list):
        raise Exception('Argument given to SQLPrepare.comma_seperate is not a list.')
    if len(items) == 0:
        return ''
    expanded_list = ''
    for i, item in enumerate(items):
        expanded_list += item
        if not i + 1 == len(items):
            expanded_list += ', '
    return expanded_list

if __name__ == "__main__":
    print(where_and(["row = ?"]))
    print(where_and(["row = ?", "anotherRow = ?"]))
    print(where_and(["row = ?", "anotherRow = ?", "thirdRow = 0"]))
    print(comma_seperate(['n = ?', 'm = 5']))
    print(comma_seperate(['n = ?']))
    # print(comma_seperate('n = 4'))
    print(comma_seperate(['n = ?', 'l = ?', 'f = ?']))