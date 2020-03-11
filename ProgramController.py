from Model import Model


class ProgramController:
    def __init__(self, theme):
        print('Controller initialized.')
        self.current_context = None
        self.model = Model()
        self.view = None
        self.set_theme(theme)

    def set_view(self, view):
        self.view = view

    def set_theme(self, name):
        self.model.set_theme(name)
        if self.view is not None:
            self.view.set_theme(self.model.theme)

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

    def get_institutions(self):
        return self.model.get_institutions()

    def switch_institution(self, institution_id):
        print('Controller switching to institution ' + str(institution_id) + '.')
        self.model.set_institution(institution_id)
        self.switch_to(self.current_context)
