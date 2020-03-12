import sqlite3
from OffBookDatabase import SQLPrepare, SQLiteTestEntries
import os

from OffBookDatabase.SQLPrepare import convert_query, append_update, append_timestamp, append_condition, \
    boolean_to_int, append_within_date_range

db = None  # The database object
dbc = None  # The database cursor
db_directory = 'data'
db_file = None
db_extension = None


def db_path():
    return db_directory + '/' + db_file + '.' + db_extension


def init_database(directory='data', file='data', extension='db'):
    """Opens the database, places in it and the cursor in memory,
    and create the db file if it doesn't exist."""
    global db, dbc, db_file, db_extension, db_directory
    db_file = file
    db_extension = extension
    db_directory = directory
    print(db_path())

    # if the db file does not exist, we have to install.
    need_to_install = False
    try:
        f = open(db_path())
        f.close()
    except IOError:
        print('need to install')
        if not os.path.exists(db_directory):
            os.mkdir(db_directory)
        need_to_install = True

    db = sqlite3.connect(db_path())
    dbc = db.cursor()
    if need_to_install:
        install_database()


def install_database():
    """Creates the tables in the database."""
    dbc.execute('''
    CREATE TABLE Institutions (
        id              INTEGER PRIMARY KEY AUTOINCREMENT,
        name            TEXT NOT NULL,
        deleted         BOOLEAN DEFAULT (false),
        lastUpdated     DATETIME DEFAULT CURRENT_TIMESTAMP
    );''')
    dbc.execute('''
    CREATE TABLE Persons(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fName TEXT DEFAULT '',
        lName TEXT DEFAULT '',
        institutionId INTEGER REFERENCES Institutions(id),
        deleted         BOOLEAN DEFAULT (false),
        lastUpdated     DATETIME DEFAULT CURRENT_TIMESTAMP
    );''')
    dbc.execute('''CREATE TABLE Productions (
        id              INTEGER  PRIMARY KEY AUTOINCREMENT,
        name            TEXT,
        description     TEXT,
        institutionId   INTEGER  REFERENCES Institutions (id),
        startDate       DATETIME,
        endDate         DATETIME,
        deleted         BOOLEAN DEFAULT (false),
        lastUpdated     DATETIME DEFAULT CURRENT_TIMESTAMP
    );
    ''')
    dbc.execute('''CREATE TABLE Events(
        id              INTEGER PRIMARY KEY AUTOINCREMENT,
        name            TEXT,
        description     TEXT,
        startDate       DATETIME,
        endDate         DATETIME,
        productionId    INTEGER REFERENCES Productions(id),
        deleted         BOOLEAN DEFAULT (false),
        lastUpdated     DATETIME DEFAULT CURRENT_TIMESTAMP
    );
    ''')
    dbc.execute('''CREATE TABLE Roles(
        id              INTEGER PRIMARY KEY AUTOINCREMENT,
        institutionId   INTEGER REFERENCES Institutions(id),
        name            TEXT,
        shortName       TEXT
    );
    ''')  # given an institutionId of 0, this role should be copied to each new institution.
    dbc.execute('''CREATE TABLE PersonProductionRoles(
        person          INTEGER REFERENCES Persons(id),
        production      INTEGER REFERENCES Productions(id),
        role            INTEGER REFERENCES Roles(id),
        lastUpdated     DATETIME DEFAULT CURRENT_TIMESTAMP
    );
    ''')
    dbc.execute('''CREATE VIEW EventsWithInstitutions AS
        SELECT Events.id as EventId, Events.name, Events.description, Events.startDate, Events.endDate,
        Events.productionId, Events.deleted, Productions.institutionId
        FROM Events JOIN Productions
        ON Productions.id == Events.productionId;''')
    dbc.execute('''
    CREATE VIEW PersonProductionRoleView AS
    SELECT personId, institutionId, productionId, Roles.id roleId, fName, lName, name roleName, shortName shortRoleName,
    lastUpdated
    FROM Roles JOIN (SELECT id personId, fName, lName, institutionId, Production productionId, role,
        max(Persons.lastUpdated, PersonProductionRoles.lastUpdated) lastUpdated
        FROM Persons JOIN PersonProductionRoles
        ON Persons.id = PersonProductionRoles.Person
        WHERE deleted = 0)
    ON role = Roles.id;''')
    SQLiteTestEntries.create(dbc)
    db.commit()


def __delete_database_file__():
    db.commit()
    db.close()
    os.remove(db_path())


def get_persons(institution_id=None, production_id=None):
    """Gets list of all persons in an institution."""
    args, conditions = [], []
    append_condition(institution_id, 'institutionId = ?', args, conditions)
    # __append_condition__(production_id, 'productionId = ?', args, conditions)
    if production_id is not None:
        print('Filtering persons by production id is not implemented yet.')
        # TODO: Write another query that filters by participation in productions.
    else:
        pass  # TODO: Push the normal query under here.
    dbc.execute('''SELECT * FROM Persons ''' + SQLPrepare.where_and(conditions) + ';', args)
    return convert_query(dbc, ['id', 'fName', 'lName', 'institutionId'])


def get_persons_updates():
    """Gets id-lastUpdated pairs for the persons table."""
    dbc.execute('SELECT (id, lastUpdated) FROM Persons')
    return convert_query(dbc, ['id', 'lastUpdated'])


def create_person(f_name, l_name, institution_id):
    """Add a new person into the database."""
    args = (f_name, l_name, institution_id)
    dbc.execute('''INSERT INTO Persons (fName, lName, institutionId)
    VALUES (?, ?, ?)''', args)
    db.commit()


def change_person(person_id, new_f_name=None, new_l_name=None):
    """Update the SQL record for a person"""
    updates, args = [], []
    append_update(new_f_name, 'fName', updates, args)
    append_update(new_l_name, 'lName', updates, args)
    append_timestamp(updates)
    args.append(person_id)
    if len(updates) > 0:
        query = 'UPDATE Persons SET ' + SQLPrepare.comma_seperate(updates) + ' WHERE id = ?;'
        dbc.execute(query, tuple(args))
        dbc.commit()


def get_productions(production_id=None, institution_id=None, date_range=None):
    """Gets a list of productions from a particular institution."""
    args, conditions = [], []
    append_condition(production_id, 'productionId = ?', args, conditions)
    append_condition(institution_id, 'institutionId = ?', args, conditions)
    append_within_date_range(date_range, args, conditions)
    query = 'SELECT * FROM Productions ' + SQLPrepare.where_and(conditions) + ';'
    dbc.execute(query, tuple(args))
    return convert_query(dbc, ['id', 'name', 'description', 'institutionId', 'startDate', 'endDate', 'deleted'])


def get_productions_updates():
    """Gets id-lastUpdated pairs for the productions table."""
    dbc.execute('SELECT (id, lastUpdated) FROM Productions')
    return convert_query(dbc, ['id', 'lastUpdated'])


def create_production(name, description, institution_id, start_date, end_date):
    """Creates a new production in the database."""
    args = (name, description, institution_id, start_date, end_date)
    dbc.execute('''INSERT INTO Productions (name, description, institutionId, startDate, endDate)
    VALUES (?, ?, ?, ?, ?)''', args)
    db.commit()


def change_production(production_id, new_name=None, new_description=None, new_start_date=None, new_end_date=None):
    """Update the SQL record for a production"""
    updates, args = [], []
    append_update(new_name, 'name', updates, args)
    append_update(new_description, 'description', updates, args)
    append_update(new_start_date, 'startDate', updates, args)
    append_update(new_end_date, 'endDate', updates, args)
    append_timestamp(updates)
    args.append(production_id)
    if len(updates) > 0:
        query = 'UPDATE Productions SET ' + SQLPrepare.comma_seperate(updates) + ' WHERE id = ?;'
        dbc.execute(query, tuple(args))
        dbc.commit()


def get_institutions():
    """Get list of institutions."""
    dbc.execute('''SELECT * FROM Institutions''')
    return convert_query(dbc, ['id', 'name'])


def get_institutions_updates():
    """Gets id-lastUpdated pairs for the persons table."""
    dbc.execute('SELECT (id, lastUpdated) FROM Institutions')
    return convert_query(dbc, ['id', 'lastUpdated'])


def create_institution(name):
    """Create an institution in the database."""
    args = (name,)
    dbc.execute('''INSERT INTO Institutions (name) VALUES (?)''', args)
    # TODO: copy roles from institution 0 to new institution
    db.commit()


def change_institution(institution_id, new_name=None):
    """Update the SQL record for an institution"""
    updates, args = [], []
    append_update(new_name, 'name', updates, args)
    append_timestamp(updates)
    args.append(institution_id)
    if len(updates) > 0:
        query = 'UPDATE Institutions SET ' + SQLPrepare.comma_seperate(updates) + ' WHERE id = ?;'
        dbc.execute(query, tuple(args))
        dbc.commit()


def get_events(institution_id=None, production_id=None, event_id=None, deleted=None, date_range=(None, None)):
    """Performs a query on events, giving back all events with certain conditions.
    Ignores the values of conditions not supplied."""
    args, conditions = [], []
    append_condition(institution_id, 'institutionId = ?', args, conditions)
    append_condition(production_id, 'productionId = ?', args, conditions)
    append_condition(event_id, 'eventId = ?', args, conditions)
    append_condition(boolean_to_int(deleted), 'deleted = ?', args, conditions)
    append_within_date_range(date_range, args, conditions)
    query = 'SELECT * FROM EventsWithInstitutions ' + SQLPrepare.where_and(conditions) + ';'
    dbc.execute(query, tuple(args))
    return convert_query(dbc, ['id', 'name', 'description', 'startDate', 'endDate', 'productionId', 'deleted',
                          'institutionId'])


def get_events_updates():
    """Gets id-lastUpdated pairs for the events table."""
    dbc.execute('SELECT (id, lastUpdated) FROM Events')
    return convert_query(dbc, ['id', 'lastUpdated'])


def create_event(name, description, start_date, end_date, production_id):
    """Create an institution in the database."""
    args = (name, description, start_date, end_date, production_id)
    dbc.execute('''INSERT INTO Institutions (name, description, startDate, endDate, productionId)
    VALUES (?, ?, ?, ?, ?);''', args)
    db.commit()


def change_event(event_id, new_name=None, new_description=None, new_start_date=None, new_end_date=None):
    """Update the SQL record for an event"""
    updates, args = [], []
    append_update(new_name, 'name', updates, args)
    append_update(new_description, 'description', updates, args)
    append_update(new_start_date, 'startDate', updates, args)
    append_update(new_end_date, 'endDate', updates, args)
    append_timestamp(updates)
    args.append(event_id)
    if len(updates) > 0:
        query = 'UPDATE Events SET ' + SQLPrepare.comma_seperate(updates) + ' WHERE id = ?;'
        dbc.execute(query, tuple(args))
        dbc.commit()


def get_roles(institution_id):
    args = (institution_id,)
    query = 'SELECT (id, name, shortName) FROM Roles WHERE institutionId = ?'
    dbc.execute(query, args)
    return convert_query(dbc, ['id', 'name', 'shortName'])


def create_role(institution_id, name, short_name=None):
    if short_name is None:
        short_name = name
    args = institution_id, name, short_name
    query = 'INSERT INTO Roles (institutionId, name, shortName) VALUES (?, ?, ?);'
    dbc.execute(query, args)
    db.commit()


def change_role(role_id, new_name=None, new_short_name=None):
    updates, args = [], []
    append_update(new_name, 'name', updates, args)
    append_update(new_short_name, 'shortName', updates, args)
    args.append(role_id)
    if len(updates) > 0:
        query = 'UPDATE Roles SET ' + SQLPrepare.comma_seperate(updates) + ' where id = ?'
        dbc.execute(query, args)
        dbc.commit()


# init_database()
# db.commit()

if __name__ == "__main__":
    # __delete_database_file__()
    init_database()
    db.commit()
    print(get_events())
    print(get_events(institution_id=0))
    print(get_events(institution_id=1))
    print(get_events(production_id=1))
    print(get_events(deleted="true"))
    print(get_events(event_id=3))
    print(get_persons())
    print(get_persons(institution_id=3))
    print(get_persons(institution_id=4))
