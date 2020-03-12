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
        view.refresh()

    def set_theme(self, name):
        self.model.set_theme(name)
        if self.view is not None:
            self.view.set_theme(self.model.theme)

    def switch_to(self, context_name):
        # print('Controller switching to "' + context_name + '".')
        if self.view is not None:
            self.view.refresh()
        self.current_context = context_name
        if context_name == 'Persons':
            self.model.query_persons()
            self.view.update_persons_frame(self.model.get_persons())
        if context_name == 'Productions':
            self.model.query_productions()
            self.view.update_productions_frame(self.model.get_productions())
        # print('Controller switched.')

    def get_persons(self):
        return self.model.get_persons()

    def get_productions(self):
        return self.model.get_productions()

    def get_institutions(self):
        return self.model.get_institutions()

    def get_events(self):
        return self.model.get_events()

    def switch_institution(self, institution_id):
        print('Controller switching to institution ' + str(institution_id) + '.')
        self.view.switch_production.delete(0, len(self.model.productions))
        self.model.set_institution(institution_id)
        self.view.configure_switch_production()
        # TODO: Switch to no production, possibly.
        self.switch_to(self.current_context)

    def switch_production(self, production_id):
        print('Controller switching to production ' + str(production_id) + '.')
        self.view.switch_event.delete(0, len(self.model.events))
        self.model.set_production(production_id)
        self.view.configure_switch_event()
        # TODO: Switch to no event, possibly.
        self.switch_to(self.current_context)

    def switch_event(self, event_id):
        print('Controller switching to event ' + str(event_id) + '.')
        self.model.set_event(event_id)

        self.switch_to(self.current_context)

    def current_institution(self):
        return self.model.current_institution()

    def current_production(self):
        return self.model.current_production()

    def current_event(self):
        return self.model.current_event()
