import SkeletonDatabase


class Model:
    def __init__(self):
        self.persons = None
        self.productions = None
        print('The model has been instantiated.')

    def query_persons(self):
        print('Query of persons...')
        self.persons = SkeletonDatabase.persons()

    def get_persons(self):
        return self.persons

    def query_productions(self):
        print('Query of productions...')
        self.productions = SkeletonDatabase.get_productions()

    def get_productions(self):
        return self.productions
