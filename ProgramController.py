from Model import Model


class ProgramController:
    def __init__(self):
        print('Controller initialized.')
        self.current_context = None
        self.model = Model()
        self.view = None

    def set_view(self, view):
        self.view = view

    def switch_to(self, context_name):
        print('Controller switching to "' + context_name + '".')
        self.current_context = context_name
        if context_name == 'Persons':
            self.model.query_persons()
            self.view.update_persons_frame(self.model.get_persons())
        if context_name == 'Productions':
            self.model.query_productions()
            self.view.update_productions_frame(self.model.get_productions())
        print('Controller switched.')

    def get_persons(self):
        return self.model.get_persons()

    def get_productions(self):
        return self.model.get_productions()
