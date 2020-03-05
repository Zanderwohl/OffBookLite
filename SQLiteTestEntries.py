def institutions(dbc):
    dbc.execute('''INSERT INTO Institutions
            (id, name) VALUES
            (0, 'None')
            ;''')
    dbc.execute('''INSERT INTO Institutions
            (id, name) VALUES
            (1, "Poppy's Pippin Troupe")
            ;''')
    dbc.execute('''INSERT INTO Institutions
            (id, name) VALUES
            (2, 'Zach Pizzaz and the Razz')
            ;''')
    dbc.execute('''INSERT INTO Institutions
            (id, name) VALUES
            (3, 'Jeffy B and Co.')
            ;''')
    dbc.execute('''INSERT INTO Institutions
            (id, name) VALUES
            (4, 'Dr. Bob')
            ;''')


def productions(dbc):
    dbc.execute('''INSERT INTO Productions
            (id, name, description, institutionId, startDate, endDate, deleted)
            VALUES
            (0, 'None', 'No Production Assigned.', 0, '1970-01-01 00:00:00', '2038-01-01 00:00:00', 0)
            ;''')
    dbc.execute('''INSERT INTO Productions
            (id, name, description, institutionId, startDate, endDate, deleted)
            VALUES
            (1, 'Pippin', 'Broadway revival Pippin.', 1, '1970-01-01 00:00:00', '2038-01-01 00:00:00', 0)
            ;''')
    dbc.execute('''INSERT INTO Productions
            (id, name, description, institutionId, startDate, endDate, deleted)
            VALUES
            (2, 'Pippin 1972', 'Original 1972 script Pippin.', 1, '1970-01-01 00:00:00', '2038-01-01 00:00:00', 0)
            ;''')
    dbc.execute('''INSERT INTO Productions
            (id, name, description, institutionId, startDate, endDate, deleted)
            VALUES
            (3, 'The Good Place', 'The Fall Show', 2, '1970-01-01 00:00:00', '2038-01-01 00:00:00', 0)
            ;''')
    dbc.execute('''INSERT INTO Productions
            (id, name, description, institutionId, startDate, endDate, deleted)
            VALUES
            (4, 'Neighborhood 12358W: The Musical', 'The Spring Musical', 2,
            '1970-01-01 00:00:00', '2038-01-01 00:00:00', 0)
            ;''')
    dbc.execute('''INSERT INTO Productions
            (id, name, description, institutionId, startDate, endDate, deleted)
            VALUES
            (5, 'Sioux Center Saga', 'Empty this string later.', 3, '1970-01-01 00:00:00', '2038-01-01 00:00:00', 0)
            ;''')
    dbc.execute('''INSERT INTO Productions
            (id, name, description, institutionId, startDate, endDate, deleted)
            VALUES
            (6, 'North-South Sudan', 'Part 2 of the saga.', 3, '1970-01-01 00:00:00', '2038-01-01 00:00:00', 0)
            ;''')


def create(dbc):
    institutions(dbc)
    productions(dbc)
    pass
