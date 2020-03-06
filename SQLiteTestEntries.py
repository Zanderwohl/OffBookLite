import csv

directory = 'test_csv'


def populate(table, dbc):
    with open(directory + '/' + table + '.csv', newline='') as csv_file:
        reader = csv.reader(csv_file)
        next(reader, None)
        for row in reader:
            query = 'INSERT INTO ' + table + ' VALUES ('
            for i in range(len(row)):
                query += '?'
                if not i + 1 == len(row):
                    query += ', '
            query += ');'
            values = tuple(row)
            # print(query, values)
            dbc.execute(query, values)


def create(dbc):
    populate('Institutions', dbc)
    populate('Productions', dbc)
    populate('Persons', dbc)
    populate('Events', dbc)


if __name__ == "__main__":
    populate('Institutions', None)
    populate('Productions', None)
    populate('Persons', None)
    populate('Events', None)
