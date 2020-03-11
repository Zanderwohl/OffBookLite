import SQLiteDatabase
import NameFinder
import Theme


class Model:
    """Manages all the data for the program, and deals with the database."""
    def __init__(self):
        self.persons = None
        self.productions = None
        self.institutions = None
        self.institution = 3
        self.events = None

        self.theme = None
        self.themes = Theme.construct_themes()

        SQLiteDatabase.init_database(file='test')
        print('Model initialized.')

    def set_theme(self, theme_name):
        self.theme = self.themes[theme_name]

    def get_themes(self):
        return list(self.themes.keys())

    def query_persons(self):
        """Load the list of persons."""
        print('Query of persons...')
        self.persons = SQLiteDatabase.get_persons(institution_id=self.institution)

    def get_persons(self):
        """Get the list of persons."""
        if self.persons is None:
            self.query_persons()
        return self.persons

    def query_productions(self):
        """Load the list of productions."""
        print('Query of productions...')
        self.productions = SQLiteDatabase.get_productions(institution_id=self.institution)

    def get_productions(self):
        """Get the list of productions."""
        if self.productions is None:
            self.query_productions()
        return self.productions

    def query_institutions(self):
        """Load the list of institutions."""
        print('Query of institutions...')
        self.institutions = SQLiteDatabase.get_institutions()

    def get_institutions(self):
        """Get the list of institutions."""
        if self.institutions is None:
            self.query_institutions()
        return self.institutions

    def query_events(self):
        """Load the list of events."""
        print('Query of events.')
        self.events = SQLiteDatabase.get_events()

    def get_events(self):
        """Get the list of events."""
        if self.events is None:
            self.query_events()
        return self.events

    def name_find(self, beginning, production=None):
        """Find persons by a name."""
        if self.persons is None:
            self.persons = SQLiteDatabase.get_persons(self.institution, production)
        return NameFinder.find(beginning, self.persons)

    def set_institution(self, institution_id):
        print('Model switching to institution ' + str(institution_id) + '.')
        ids = [inst['id'] for inst in self.get_institutions()]  # get all id for institutions.
        print(ids)
        if institution_id not in ids:
            raise Exception('Id ' + institution_id + ' is not an existing institution.')
        self.institution = institution_id
        self.query_productions()
        self.query_events()
        self.query_persons()

