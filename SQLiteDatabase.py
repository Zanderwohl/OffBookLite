import sqlite3

db = None   # The database object
dbc = None  # The database cursor
db_file = 'test.db'


def init_database():
    """Opens the database, places in it and the cursor in memory,
    and create the db file if it doesn't exist."""
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
    """Creates the tables in the database."""
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
    """Takes the results of a query (stored in this file's scope)
    and turns it into an array of dictionaries."""
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


def get_persons(institution_id, production_id):
    """Gets list of all persons in an institution."""
    if production_id is not None:
        print('Filtering persons by production id is not implemented yet.')
        # TODO: Write another query that filters by participation in productions.
    else:
        pass    # TODO: Push the normal query under here.
    args = (institution_id,)
    dbc.execute('''SELECT * FROM Persons
    WHERE institutionId=?''', args)
    return convert_query(['id', 'fName', 'lName', 'institutionId'])


def create_person(f_name, l_name, institution_id):
    """Add a new person into the database."""
    args = (f_name, l_name, institution_id)
    dbc.execute('''INSERT INTO Persons (fName, lName, institutionId)
    VALUES (?, ?, ?)''', args)
    db.commit()


def get_productions(production_id=None):
    """Gets a list of productions from a particular institution."""
    if production_id is not None:
        args = (production_id,)
        dbc.execute('''SELECT * FROM Productions
        WHERE productionId = ?
        ''', args)
    else:
        dbc.execute('''SELECT * FROM Productions''')
    return convert_query(['id', 'name', 'description', 'institutionId', 'startDate', 'endDate', 'deleted'])


def create_production(name, description, institution_id, start_date, end_date):
    """Creates a new production in the database."""
    args = (name, description, institution_id, start_date, end_date)
    dbc.execute('''INSERT INTO Productions (name, description, institutionId, startDate, endDate)
    VALUES (?, ?, ?, ?, ?)''', args)
    db.commit()


def get_institutions():
    """Get list of institutions."""
    dbc.execute('''SELECT * FROM Institutions''')
    return convert_query(['id', 'name'])


def create_institution(name):
    """Create an institution in the database."""
    args = (name,)
    dbc.execute('''INSERT INTO Institutions (name) VALUES (?)''', args)
    db.commit()


init_database()
db.commit()
