from tkinter import Menu


class DropdownManager:
    def __init__(self, window, controller, master, institutions, productions, events):
        self.menu_bar = Menu(master)
        self.window = window
        self.controller = controller
        master.config(menu=self.menu_bar)
        self.__add_file__(window)
        self.__add_context__(window)
        self.__add_navigate__(window, controller, institutions, productions, events)

    def __add_file__(self, window):
        file_menu = Menu(self.menu_bar, tearoff=0)
        file_menu.add_separator()
        file_menu.add_command(label='Exit', command=window.v_exit)
        self.menu_bar.add_cascade(label='File', menu=file_menu)

    def __add_context__(self, window):
        context_menu = Menu(self.menu_bar, tearoff=0)
        context_menu.add_command(label="Main Menu", command=lambda: window.show_frame('Menu'))
        context_menu.add_command(label="Persons", command=lambda: window.show_frame('Persons'))
        context_menu.add_command(label="Institutions", command=lambda: window.show_frame('Institutions'))
        context_menu.add_command(label="Productions", command=lambda: window.show_frame('Productions'))
        context_menu.add_command(label="Events", command=lambda: window.show_frame('Events'))
        self.menu_bar.add_cascade(label="Context", menu=context_menu)

    def __add_navigate__(self, window, controller, institutions, productions, events):
        self.switch_institution = None
        self.institutions_num = 0
        self.switch_production = None
        self.productions_num = 0
        self.switch_event = None
        self.events_num = 0
        navigate_menu = Menu(self.menu_bar, tearoff=0)
        self.switch_institution = Menu(navigate_menu, tearoff=0)
        navigate_menu.add_cascade(label='Switch Institution', menu=self.switch_institution)
        self.switch_production = Menu(navigate_menu, tearoff=0)
        navigate_menu.add_cascade(label='Switch Production', menu=self.switch_production)
        self.switch_event = Menu(navigate_menu, tearoff=0)
        navigate_menu.add_cascade(label='Switch Event', menu=self.switch_event)
        self.configure_switch_institution(institutions)
        self.configure_switch_production(productions)
        self.configure_switch_event(events)
        self.menu_bar.add_cascade(label='Navigate', menu=navigate_menu)

    def configure_switch_institution(self, institutions):
        self.switch_institution.delete(0, self.institutions_num)
        institutions = institutions.items()
        self.institutions_num = len(institutions)
        for _id, institution in institutions:
            if not institution['id'] == 0:
                self.switch_institution.add_cascade(label=institution['name'],
                                                    command=lambda inst_id=institution['id']:
                                                    self.controller.switch_institution(inst_id))

    def configure_switch_production(self, productions):
        self.switch_production.delete(0, self.productions_num)
        productions = productions.items()
        self.productions_num = len(productions)
        for _id, production in productions:
            self.switch_production.add_cascade(label=production['name'],
                                               command=lambda prod_id=production['id']:
                                               self.controller.switch_production(prod_id))

    def configure_switch_event(self, events):
        self.switch_event.delete(0, self.events_num)
        events = events.items()
        self.events_num = len(events)
        for _id, event in events:
            self.switch_event.add_cascade(label=event['startDate'] + ' ' + event['name'],
                                          command=lambda event_id=event['id']:
                                          self.controller.switch_event(event_id))
