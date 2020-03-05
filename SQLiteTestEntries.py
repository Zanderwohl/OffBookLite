import csv

directory = 'test_csv'


def institutions(dbc):
    with open(directory + '/institutions.csv', newline='') as csv_file:
        reader = csv.reader(csv_file)
        next(reader, None)
        for row in reader:
            dbc.execute('''INSERT INTO Institutions VALUES (?, ?, ?);''', tuple(row))


def productions(dbc):
    with open(directory + '/productions.csv', newline='') as csv_file:
        reader = csv.reader(csv_file)
        next(reader, None)
        for row in reader:
            dbc.execute('''INSERT INTO Productions VALUES (?, ?, ?, ?, ?, ?, ?);''', tuple(row))


def productions(dbc):
    with open(directory + '/persons.csv', newline='') as csv_file:
        reader = csv.reader(csv_file)
        next(reader, None)
        for row in reader:
            dbc.execute('''INSERT INTO Persons VALUES (?, ?, ?, ?, ?);''', tuple(row))


def create(dbc):

    institutions(dbc)
    productions(dbc)
    pass


if __name__ == "__main__":
    institutions(None)