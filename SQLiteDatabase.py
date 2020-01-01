import sqlite3

db = None   # The database object
dbc = None  # The database cursor
db_file = 'test.db'


def init_database():
    global db, dbc

    # if the db file does not exist, we have to install.
    need_to_install = False
    try:
        f = open(db_file)
        f.close()
    except IOError:
        print('need to install')
        need_to_install = True

    db = sqlite3.connect(db_file)
    dbc = db.cursor()
    if need_to_install:
        install_database()


def install_database():
    dbc.execute('''
    CREATE TABLE Institutions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )''')
    dbc.execute('''
    CREATE TABLE Persons(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fName TEXT DEFAULT '',
        lName TEXT DEFAULT '',
        institutionId INT NOT NULL,
        FOREIGN KEY (institutionId) REFERENCES Institutions(id)
    )''')
    db.commit()


def convert_query(keys):
    query = []
    while True:
        next_row = dbc.fetchone()
        # print(next_row)
        # print(keys)
        if next_row is None:
            break
        next_row_dictionary = {}
        for entry, key in zip(next_row, keys):
            next_row_dictionary.update({key: entry})
        query.append(next_row_dictionary)
#    print(query)
    return query


def get_persons(institution_id):
    args = (institution_id,)
    dbc.execute('''SELECT * FROM Persons
    WHERE institutionId=?''', args)
    return convert_query(['id', 'fName', 'lName', 'institutionId'])

# init_database()
# install_database()
