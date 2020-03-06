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

if __name__ == "__main__":
    print(where_and(["row = ?"]))
    print(where_and(["row = ?", "anotherRow = ?"]))
    print(where_and(["row = ?", "anotherRow = ?", "thirdRow = 0"]))