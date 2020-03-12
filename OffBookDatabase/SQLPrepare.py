

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


def comma_separate(items):
    if not isinstance(items, list):
        raise Exception('Argument given to SQLPrepare.comma_separate is not a list.')
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
    print(comma_separate(['n = ?', 'm = 5']))
    print(comma_separate(['n = ?']))
    # print(comma_seperate('n = 4'))
    print(comma_separate(['n = ?', 'l = ?', 'f = ?']))


def convert_query(dbc, keys):
    """Takes the results of a query (stored in this file's scope)
    and turns it into an array of dictionaries."""
    # query = []
    query = {}
    while True:
        next_row = dbc.fetchone()
        # print(next_row)
        # print(keys)
        if next_row is None:
            break
        next_row_dictionary = {}
        for entry, key in zip(next_row, keys):
            next_row_dictionary.update({key: entry})
        # print(next_row_dictionary['id'])
        query[next_row_dictionary['id']] = next_row_dictionary
    return query


def append_update(new_value, column_name, updates, args):
    if new_value is not None:
        updates.append(column_name + ' = ?')
        args.append(new_value)


def append_timestamp(updates):
    updates.append('lastUpdated = CURRENT_TIMESTAMP')


def append_condition(arg, condition, args, conditions):
    """Helper function for get_events.
    arg is the value to be compared,
    condition is the conditional statement the arg will be placed into,
    (like 'columnName =?')
    args is the list of args this argument should be added to,
    and conditions is the list of condition strings."""
    if arg is not None:
        args.append(arg)
        conditions.append(condition)


def boolean_to_int(value):
    """Prepares a true or false value, whether string or boolean, for sql, which requires an integer."""
    if value == "true" or value == "True" or value is True:
        return 1
    if value == "false" or value == "False" or value is False:
        return 0
    if value is None:
        return None


def append_within_date_range(date_range, args, conditions):
    """Appends a speical condition that ensures an event falls within (inclusive) a date range."""
    if date_range is not None and len(date_range) == 2:
        start_date, end_date = date_range
        if len(date_range) == 2 and start_date is not None and end_date is not None:
            args.append(start_date)
            args.append(start_date)
            args.append(end_date)
            args.append(end_date)
            conditions.append('(startDate >= ? OR endDate >= ?) AND (startDate <= ? or endDate <= ?)')
