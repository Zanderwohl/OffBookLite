import SQLiteDatabase
import SkeletonDatabase


class Model:
    def __init__(self):
        self.persons = None
        self.productions = None
        self.institution = 3
        SQLiteDatabase.init_database()
        print('Model initialized.')

    def query_persons(self):
        print('Query of persons...')
        self.persons = SQLiteDatabase.get_persons(self.institution)

    def get_persons(self):
        return self.persons

    def query_productions(self):
        print('Query of productions...')
        self.productions = SkeletonDatabase.get_productions()

    def get_productions(self):
        return self.productions
