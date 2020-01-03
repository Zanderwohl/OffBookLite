import SQLiteDatabase
import SkeletonDatabase
import NameFinder


class Model:
    def __init__(self):
        self.persons = None
        self.productions = None
        self.institutions = None
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
        self.productions = SQLiteDatabase.get_productions()

    def get_productions(self):
        return self.productions

    def get_institutions(self):
        print('Query of institutions...')
        self.institutions = SQLiteDatabase.get_institutions()

    def name_find(self, beginning, production=None):
        return NameFinder.find(beginning, production)
