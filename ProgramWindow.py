from tkinter import *

from OffBookGUI.Clocks import TimeClock, DateClock
from OffBookGUI.DropdownManager import DropdownManager
from OffBookGUI.EventFrame import EventFrame
from OffBookGUI.InstitutionFrame import InstitutionFrame
from OffBookGUI.Locator import Locator
from OffBookGUI.PersonFrame import PersonFrame
from OffBookGUI.ProductionFrame import ProductionFrame
from OffBookGUI.QOTD import QOTD
from OffBookGUI.ScrollFrame import ScrollFrame


class Window(Frame):

    def __init__(self, master, controller):
        Frame.__init__(self, master)
        self.master = master
        self.controller = controller
        self.theme = self.controller.current_theme()
        self.frames = {}
        self.current_frame = None
        self.drop = DropdownManager(self, controller, master,
                                    controller.get_institutions(),
                                    controller.get_productions(),
                                    controller.get_events())
        self.location = None

        self.pack(side="top", fill="both", expand=True)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.add_context_switcher()
        self.add_menu_frame()
        self.add_persons_frame()
        self.persons_frames = []
        self.add_institutions_frame()
        self.institutions_frames = []
        self.add_productions_frame()
        self.productions_frames = []
        self.add_events_frame()
        self.events_frames = []

        self.show_frame('Menu')

    def switch_institution(self, productions):
        self.drop.configure_switch_production(productions)

    def switch_production(self, events):
        self.drop.configure_switch_event(events)

    def add_context_switcher(self):
        context_switcher = Frame(self, bg=self.theme['Tabs Background'])
        context_switcher.pack(side=BOTTOM, fill=BOTH)
        self.add_context_button(context_switcher, 'Home', 'Menu')
        self.add_context_button(context_switcher, 'Persons', 'Persons')
        self.add_context_button(context_switcher, 'Institutions', 'Institutions')
        self.add_context_button(context_switcher, 'Productions', 'Productions')
        self.add_context_button(context_switcher, 'Events', 'Events')
        self.location = Locator(context_switcher, self.theme)
        self.location.pack()
        time_frame = Frame(context_switcher, bg=self.theme['Background'])
        time_frame.pack()
        clock = TimeClock(time_frame, self.theme)
        date = DateClock(time_frame, self.theme)
        date.pack()
        clock.pack()
        self.frames.update({'Context Switcher': context_switcher})

    def add_context_button(self, context_switcher, text, frame_name):
        button = Button(context_switcher, text=text, command=lambda: self.show_frame(frame_name),
                        height=2, bg=self.theme['Button Background'], fg=self.theme['Button Foreground'])
        button.pack(side=LEFT, padx=10, pady=10)

    def v_exit(self):
        self.controller.close_program(origin='ProgramWindow')

    def add_menu_frame(self):
        main_menu_frame = Frame(self, bg=self.theme['Background'])
        quote_of_the_day = QOTD(main_menu_frame, self.theme, self.controller.get_quotes())
        quote_of_the_day.pack()
        self.frames.update({'Menu': main_menu_frame})

    def add_persons_frame(self):
        persons_frame = Frame(self, bg=self.theme['Background'])
        self.frames['Persons List'] = None
        self.frames.update({'Persons': persons_frame})

    def update_persons_frame(self, persons):
        self.reset_frame('Persons List', 'Persons')

        self.persons_frames = []

        # print(persons)
        for i, key in enumerate(persons):
            meta_frame, person_frame = self.add_person_frame(persons[key],
                                                             self.frames['Persons List'].child_frame, i)
            # print(person_frame)
            self.persons_frames.append(person_frame)
            meta_frame.pack(fill=X, expand=True)

    def add_person_frame(self, person, parent, index):
        if index % 2 == 0:
            color = self.theme['List A']
        else:
            color = self.theme['List B']
        meta_frame = Frame(parent)
        person_frame = PersonFrame(person, self, self.theme, meta_frame, color=color)
        return meta_frame, person_frame

    def add_institutions_frame(self):
        institutions_frame = Frame(self, bg=self.theme['Background'])
        self.frames['Institutions List'] = None
        self.frames.update({'Institutions': institutions_frame})

    def update_institutions_frame(self, institutions):
        self.reset_frame('Institutions List', 'Institutions')

        self.institutions_frames = []

        for i, key in enumerate(institutions):
            meta_frame, institution_frame = self.add_institution_frame(institutions[key],
                                                                       self.frames['Institutions List'].child_frame, i)
            self.persons_frames.append(institution_frame)
            meta_frame.pack(fill=X, expand=True)

    def add_institution_frame(self, institution, parent, index):
        if index % 2 == 0:
            color = self.theme['List A']
        else:
            color = self.theme['List B']
        meta_frame = Frame(parent)
        person_frame = InstitutionFrame(institution, self, self.theme, meta_frame, color)
        return meta_frame, person_frame

    def add_productions_frame(self):
        productions_frame = Frame(self, bg=self.theme['Background'])
        self.frames['Productions List'] = None
        self.frames.update({'Productions': productions_frame})

    def update_productions_frame(self, productions):
        self.reset_frame('Productions List', 'Productions')

        self.productions_frames = []

        for i, key in enumerate(productions.keys()):
            meta_frame, prod_frame = self.add_production_frame(productions[key],
                                                               self.frames['Productions List'].child_frame, i)
            self.productions_frames.append(prod_frame)
            meta_frame.pack(fill=X, expand=True)

    def add_production_frame(self, person, parent, index):
        if index % 2 == 0:
            color = self.theme['List A']
        else:
            color = self.theme['List B']
        meta_frame = Frame(parent)
        production_frame = ProductionFrame(person, self, self.theme, meta_frame, color=color)
        return meta_frame, production_frame

    def add_events_frame(self):
        events_frame = Frame(self, bg=self.theme['Background'])
        self.frames['Events List'] = None
        self.frames.update({'Events': events_frame})

    def update_events_frame(self, events):
        self.reset_frame('Events List', 'Events')

        self.events_frames = []

        for i, key in enumerate(events.keys()):
            meta_frame, event_frame = self.add_event_frame(events[key], self.frames['Events List'].child_frame, i)
            self.events_frames.append(event_frame)
            meta_frame.pack(fill=X, expand=True)

    def add_event_frame(self, event, parent, index):
        if index % 2 == 0:
            color = self.theme['List A']
        else:
            color = self.theme['List B']
        meta_frame = Frame(parent)
        event_frame = EventFrame(event, self, self.theme, meta_frame, color)
        return meta_frame, event_frame

    def show_frame(self, name):
        # print('Window switching to frame "' + name + '".')
        self.controller.switch_to(name)
        if self.current_frame is not None:
            self.current_frame.pack_forget()
        frame = self.frames[name]
        self.current_frame = frame
        frame.pack(fill=BOTH, expand=True)
        # print('Window switched.')

    def set_theme(self, theme):
        self.theme = theme

    def refresh(self):
        self.location.update(self.controller.current_institution(),
                             self.controller.current_production(),
                             self.controller.current_event())

    def reset_frame(self, frame_name, frame_parent):
        if self.frames[frame_name] is not None:
            self.frames[frame_name].pack_forget()
            self.frames[frame_name].destroy()
            self.frames[frame_name] = None
        self.frames[frame_name] = ScrollFrame(self, holder_frame=self.frames[frame_parent])
        # self.frames[frame_name] = Frame(self)
        self.frames[frame_name].pack(fill=BOTH, expand=True)

    def list_color(self, index):
        if index % 2 == 0:
            return self.theme['List A']
        else:
            return self.theme['List B']


def show_window(controller):
    root = Tk()
    root.protocol("WM_DELETE_WINDOW", controller.close_program)
    app = Window(root, controller)

    root.wm_title("OffBook Lite")
    # root.geometry("320x200");

    # Sets minimum window size.
    root.update()
    root.minsize(root.winfo_width(), root.winfo_height())

    # root.attributes('-fullscreen', True)  #fullscreens the window

    # w, h = root.winfo_screenwidth(), root.winfo_screenheight()  #resizes window to screen size
    # root.geometry("%dx%d+0+0" % (w, h))

    root.state('zoomed')  # maximizes window

    controller.set_view(app)  # give this to the controller

    root.mainloop()  # show window

    return root, app
