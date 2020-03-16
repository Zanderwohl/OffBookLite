from OffBookDatabase import SQLiteDatabase
import NameFinder
from OffBookGUI import Theme


class Model:
    """Manages all the data for the program, and deals with the database."""
    def __init__(self, settings):
        self.persons = None
        self.productions = None
        self.institutions = None
        self.events = None
        self.quotes = None

        self.institution = 0
        self.production = None
        self.event = None

        self.theme = None
        self.themes = Theme.construct_themes()

        reset = settings.get('reset', False)
        SQLiteDatabase.init_database(file='test', reset=reset)
        print('Model initialized.')

    def close(self):
        SQLiteDatabase.close()

    def current_institution(self):
        try:
            return self.institutions[self.institution]
        except KeyError:
            return None

    def current_production(self):
        try:
            return self.productions[self.production]
        except KeyError:
            return None

    def current_event(self):
        try:
            return self.events[self.event]
        except KeyError:
            return None

    def set_theme(self, theme_name):
        self.theme = self.themes[theme_name]

    def current_theme(self):
        return self.theme

    def get_themes(self):
        return list(self.themes.keys())

    def query_persons(self):
        """Load the list of persons."""
        # print('Query of persons...')
        self.persons = SQLiteDatabase.get_persons(institution_id=self.institution)

    def get_persons(self):
        """Get the list of persons."""
        if self.persons is None:
            self.query_persons()
        return self.persons

    def query_productions(self):
        """Load the list of productions."""
        # print('Query of productions...')
        self.productions = SQLiteDatabase.get_productions(institution_id=self.institution)

    def get_productions(self):
        """Get the list of productions."""
        if self.productions is None:
            self.query_productions()
        return self.productions

    def query_institutions(self):
        """Load the list of institutions."""
        # print('Query of institutions...')
        self.institutions = SQLiteDatabase.get_institutions()

    def get_institutions(self):
        """Get the list of institutions."""
        if self.institutions is None:
            self.query_institutions()
        return self.institutions

    def query_events(self):
        """Load the list of events."""
        # print('Query of events.')
        self.events = SQLiteDatabase.get_events(production_id=self.production, institution_id=self.institution)

    def get_events(self):
        """Get the list of events."""
        if self.events is None:
            self.query_events()
        return self.events

    def query_quotes(self):
        """Load this list of quotes."""
        self.quotes = SQLiteDatabase.get_quotes()

    def get_quotes(self):
        """Get the list of quotes."""
        if self.quotes is None:
            self.query_quotes()
        return self.quotes

    def name_find(self, beginning, production_id):
        """Find persons by a name."""
        if self.persons is None:
            self.persons = SQLiteDatabase.get_persons(self.institution, production_id=production_id)
        return NameFinder.find_person(beginning, self.persons, production_id=production_id)

    def production_find(self, text, institution=None):
        """Find productions by a name or description text."""
        if self.productions is None:
            self.productions = SQLiteDatabase.get_productions(institution_id=self.institution)
        return NameFinder.find_production(text, self.productions, institution_id=institution)

    def set_institution(self, institution_id):
        print('Model switching to institution ' + str(institution_id) + '.')
        ids = self.get_institutions().keys()  # get all id for institutions.
        # print(ids)
        if institution_id not in ids:
            first_institution = list(self.get_institutions().values())[1]['id']
            print(first_institution)
            self.set_institution(first_institution)
            return
            # raise Exception('Id ' + institution_id + ' is not an existing institution.')
        self.institution = institution_id
        self.query_productions()
        self.query_events()
        self.query_persons()

    def set_production(self, production_id):
        print('Model switching to production ' + str(production_id) + '.')
        ids = self.get_productions().keys()
        # print(ids)
        if production_id not in ids:
            first_production = list(self.get_productions().values())[0]['id']
            self.set_production(first_production)
            return
            # raise Exception('Id ' + production_id + ' is not an existing production.')
        self.production = production_id
        self.query_events()
        self.query_persons()

    def set_event(self, event_id):
        print('Model switching to event ' + str(event_id) + '.')
        ids = self.get_events().keys()
        # print(ids)
        if event_id not in ids:
            first_event = list(self.get_events().values())[0]['id']
            self.set_event(first_event)
            return
            # raise Exception('Id ' + event_id + ' is not an existing event.')
        self.event = event_id
        self.query_persons()
