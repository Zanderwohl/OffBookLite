import SkeletonDatabase


class Model:
    def __init__(self):
        self.persons = None
        print('The model has been instantiated.')

    def query_persons(self):
        print('Query of persons...')
        self.persons = SkeletonDatabase.persons()

    def get_persons(self):
        return self.persons
