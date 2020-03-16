from tkinter import *

from OffBookGUI.Clocks import TimeClock, DateClock
from OffBookGUI.DropdownManager import DropdownManager
from OffBookGUI.Locator import Locator
from OffBookGUI.PersonFrame import PersonFrame
from OffBookGUI.ProductionFrame import ProductionFrame


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
        self.productions_frames = []
        self.add_institutions_frame()
        self.add_productions_frame()
        self.add_events_frame()

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

    def add_calc_drop(self):
        calc_menu = Menu(self.menu)
        calc_menu.add_command(label="Torch Burn")
        calc_menu.add_command(label="Hohmann Transfer")
        calc_menu.add_separator()
        calc_menu.add_command(label="Radio Time")
        self.menu.add_cascade(label="Calculate", menu=calc_menu)

    def v_exit(self):
        self.controller.close_program(origin='ProgramWindow')

    def add_menu_frame(self):
        main_menu_frame = Frame(self, bg=self.theme['Background'])
        button_persons = Button(main_menu_frame, text='Persons', command=lambda: self.show_frame('Persons'))
        button_persons.pack()
        button_institutions = Button(main_menu_frame, text="Institutions",
                                     command=lambda: self.show_frame('Institutions'))
        button_institutions.pack()
        self.frames.update({'Menu': main_menu_frame})

    def add_persons_frame(self):
        persons_frame = Frame(self, bg=self.theme['Background'])
        self.frames['Persons List'] = None
        self.frames.update({'Persons': persons_frame})

    def update_persons_frame(self, persons):
        if self.frames['Persons List'] is not None:
            # print("Replacing it!")
            self.frames['Persons List'].pack_forget()
            self.frames['Persons List'].destroy()

        self.frames['Persons List'] = Frame(self.frames['Persons'])
        self.frames['Persons List'].pack(fill=X)

        persons = self.controller.get_persons()

        self.persons_frames = []

        # print(persons)
        for i, key in enumerate(persons):
            meta_frame, person_frame = self.add_person_frame(persons[key], self.frames['Persons List'], i)
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
        button = Button(institutions_frame, text='You\'re in Institutions')
        button.pack()
        self.frames.update({'Institutions': institutions_frame})

    def add_productions_frame(self):
        productions_frame = Frame(self, bg=self.theme['Background'])
        self.frames['Productions List'] = None
        self.frames.update({'Productions': productions_frame})

    def update_productions_frame(self, productions):
        if self.frames['Productions List'] is not None:
            print("Replacing it!")
            self.frames['Productions List'].pack_forget()
            self.frames['Productions List'].destroy()

        self.frames['Productions List'] = Frame(self.frames['Productions'])
        self.frames['Productions List'].pack(fill=X)

        # productions = self.controller.get_productions()

        self.productions_frames = []

        for i, key in enumerate(productions.keys()):
            meta_frame, production_frame = self.add_production_frame(productions[key], self.frames['Productions List'], i)
            self.persons_frames.append(production_frame)
            meta_frame.pack(fill=X, expand=True)

    def add_production_frame(self, person, parent, index):
        if index % 2 == 0:
            color = self.theme['List A']
        else:
            color = self.theme['List B']

        meta_frame = Frame(parent)
        production_frame = ProductionFrame(person, self, self.theme, meta_frame, color=color)
        return meta_frame, production_frame

    def generate_production_frame_small(self, production, parent, index, meta_frame, old_frame, color):
        if old_frame is not None:
            old_frame.pack_forget()
        frame = Frame(meta_frame, bg=color)
        frame.columnconfigure(1, weight=1)
        frame.columnconfigure(2, weight=2)
        frame.columnconfigure(3, weight=1)
        name_text = production['name']
        name_label = Label(frame, text=name_text, padx=10, pady=10, bg=color, fg=self.theme['Text'])
        name_label.grid(column=1, row=0)
        expand_button = Button(frame, text='More', padx=10,
                               command=lambda: self.generate_production_frame_large(
                                   production, parent, index, meta_frame, frame, color))
        expand_button.grid(column=3, row=0)
        # new_button.grid(column=0, row=index)
        frame.pack(fill=X, expand=True)
        return frame

    def generate_production_frame_large(self, production, parent, index, meta_frame, old_frame, color):
        if old_frame is not None:
            old_frame.pack_forget()
        frame = Frame(meta_frame, bg=color)
        frame.columnconfigure(1, weight=1)
        frame.columnconfigure(2, weight=2)
        frame.columnconfigure(3, weight=1)
        frame.rowconfigure(0, weight=1)
        frame.rowconfigure(1, weight=1)
        frame.rowconfigure(2, weight=1)
        frame.rowconfigure(3, weight=1)
        frame.rowconfigure(5, weight=1)
        name_text = production['name']
        name_label = Label(frame, text=name_text, padx=10, pady=60, bg=color, fg=self.theme['Text'])
        name_label.grid(column=1, row=0)
        expand_button = Button(frame, text='Less', padx=10,
                               command=lambda: self.generate_production_frame_small(
                                   production, parent, index, meta_frame, frame, color))
        expand_button.grid(column=3, row=0)
        # new_button.grid(column=0, row=index)
        frame.pack(fill=X, expand=True)

    def add_events_frame(self):
        events_frame = Frame(self, bg=self.theme['Background'])
        button = Button(events_frame, text='You\'re in Events')
        button.pack()
        self.frames.update({'Events': events_frame})

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
