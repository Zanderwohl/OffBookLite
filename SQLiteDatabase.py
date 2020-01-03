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
    );''')
    dbc.execute('''
    CREATE TABLE Persons(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fName TEXT DEFAULT '',
        lName TEXT DEFAULT '',
        institutionId INT NOT NULL,
        FOREIGN KEY (institutionId) REFERENCES Institutions(id)
    );''')
    dbc.execute('''CREATE TABLE Productions (
        id            INTEGER  PRIMARY KEY,
        name          TEXT,
        description   TEXT,
        institutionId INTEGER  REFERENCES Institutions (id),
        startDate     DATETIME,
        endDate       DATETIME,
        deleted       BOOLEAN  DEFAULT (false) 
    );
    ''')
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


def create_person(f_name, l_name, institution_id):
    args = (f_name, l_name, institution_id)
    dbc.execute('''INSERT INTO Persons (fName, lName, institutionId)
    VALUES (?, ?, ?)''', args)
    db.commit()


def get_productions(production_id=None):
    if production_id is not None:
        args = (production_id,)
        dbc.execute('''SELECT * FROM Productions
        WHERE productionId = ?
        ''', args)
    else:
        dbc.execute('''SELECT * FROM Productions''')
    return convert_query(['id', 'name', 'description', 'institutionId', 'startDate', 'endDate', 'deleted'])


def create_production(name, description, institution_id, start_date, end_date):
    args = (name, description, institution_id, start_date, end_date)
    dbc.execute('''INSERT INTO Productions (name, description, institutionId, startDate, endDate)
    VALUES (?, ?, ?, ?, ?)''', args)
    db.commit()


def get_institutions():
    dbc.execute('''SELECT * FROM Institutions''')
    return convert_query(['id', 'name'])


def create_institution(name):
    args = (name,)
    dbc.execute('''INSERT INTO Institutions (name) VALUES (?)''', args)
    db.commit()


init_database()
# create_institution('Something Else')
# create_production('Something Rotten', 'A musical I liked very much',
#                  2, '0', '0') # 2008-11-11 13:23:44
# create_person('Rachel', 'Smort', 2)
db.commit()
# install_database()
