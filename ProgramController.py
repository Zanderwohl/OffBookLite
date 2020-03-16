import sys

from Model import Model


def load_settings(config_file_name):
    try:
        config = open(config_file_name, 'r')
        settings = {}
        for line in config:
            pair = line.split('=')
            if len(pair) == 2:
                key, value = pair
                settings[key] = value.strip()
        config.close()
        return settings
    except FileNotFoundError:
        config = open(config_file_name, 'w')
        config.write('Theme=Dark\nInstitution=0\nProduction=0\nEvent=0')  # TODO: Make this more generalized.
        config.close()
        return load_settings(config_file_name)


class ProgramController:
    def __init__(self):
        print('Controller initialized.')
        self.current_context = None
        self.model = Model()
        self.settings = load_settings('settings.config')
        self.set_settings()
        self.view = None
        self.set_theme(self.settings['Theme'])

    def set_settings(self):
        self.model.query_institutions()
        # print(self.model.get_institutions())
        self.model.set_institution(int(self.settings['Institution']))
        self.model.set_production(int(self.settings['Production']))
        self.model.set_event(int(self.settings['Event']))

    def close_program(self, status=0, origin=None):
        self.save_settings('settings.config')
        sys.exit(0)

    def save_settings(self, config_file_name):
        self.settings['Institution'] = self.model.institution
        self.settings['Production'] = self.model.production
        self.settings['Event'] = self.model.event
        config = open(config_file_name, 'w')
        for key in self.settings:
            config.write(key + '=' + str(self.settings[key]) + '\n')
        config.close()

    def set_view(self, view):
        self.view = view
        view.refresh()

    def set_theme(self, name):
        self.model.set_theme(name)
        if self.view is not None:
            self.view.set_theme(self.model.theme)

    def current_theme(self):
        return self.model.current_theme()

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

    def get_quotes(self):
        return self.model.get_quotes()

    def switch_institution(self, institution_id):
        print('Controller switching to institution ' + str(institution_id) + '.')
        self.model.set_institution(institution_id)
        self.view.switch_institution(self.get_productions())
        self.switch_to(self.current_context)

    def switch_production(self, production_id):
        print('Controller switching to production ' + str(production_id) + '.')
        self.model.set_production(production_id)
        self.view.switch_production(self.get_events())
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
