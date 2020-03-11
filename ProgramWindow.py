from tkinter import *


class Window(Frame):

    def __init__(self, master, controller):
        Frame.__init__(self, master)
        self.master = master
        self.controller = controller
        self.frames = {}
        self.current_frame = None
        self.menu = None
        self.switch_institution = None

        self.pack(side="top", fill="both", expand=True)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.add_menu_bar()

        self.add_context_drop()
        self.add_navigate_drop()

        self.add_context_switcher()
        self.add_menu_frame()
        self.add_persons_frame()
        self.add_institutions_frame()
        self.add_productions_frame()
        self.add_events_frame()

        self.show_frame('Menu')

    def add_menu_bar(self):
        self.menu = Menu(self.master)
        self.master.config(menu=self.menu)

    def add_context_drop(self):
        context_menu = Menu(self.menu)
        context_menu.add_command(label="Main Menu", command=lambda: self.show_frame('Menu'))
        context_menu.add_command(label="Persons", command=lambda: self.show_frame('Persons'))
        context_menu.add_command(label="Institutions", command=lambda: self.show_frame('Institutions'))
        self.menu.add_cascade(label="Context", menu=context_menu)

    def add_navigate_drop(self):
        navigate_menu = Menu(self.master)
        self.switch_institution = Menu(self.master)
        navigate_menu.add_cascade(label="Switch Institution", menu=self.switch_institution)
        self.configure_switch_institution()
        self.menu.add_cascade(label="Navigate", menu=navigate_menu)

    def configure_switch_institution(self):
        institutions = self.controller.get_institutions()
        for institution in institutions:
            if institution['id'] is not 0:
                self.switch_institution.add_cascade(label=institution['name'],
                                                    command=lambda inst_id=institution['id']:
                                                    self.controller.switch_institution(inst_id))

    def add_context_switcher(self):
        context_switcher = Frame(self, bg="#232323")
        context_switcher.pack(side=BOTTOM, fill=BOTH)
        self.add_context_button(context_switcher, 'Home', 'Menu')
        self.add_context_button(context_switcher, 'Persons', 'Persons')
        self.add_context_button(context_switcher, 'Institutions', 'Institutions')
        self.add_context_button(context_switcher, 'Productions', 'Productions')
        self.add_context_button(context_switcher, 'Events', 'Events')
        self.frames.update({'Context Switcher': context_switcher})

    def add_context_button(self, context_switcher, text, frame_name):
        button = Button(context_switcher, text=text, command=lambda: self.show_frame(frame_name),
                        height=2, bg="#555555", fg="#DDDDDD")
        button.pack(side=LEFT, padx=10, pady=10)

    def add_calc_drop(self):
        calc_menu = Menu(self.menu)
        calc_menu.add_command(label="Torch Burn")
        calc_menu.add_command(label="Hohmann Transfer")
        calc_menu.add_separator()
        calc_menu.add_command(label="Radio Time")
        self.menu.add_cascade(label="Calculate", menu=calc_menu)

    def v_exit(self):
        self.controller.exit(1)

    def add_menu_frame(self):
        main_menu_frame = Frame(self, bg='#555555')
        button_persons = Button(main_menu_frame, text='Persons', command=lambda: self.show_frame('Persons'))
        button_persons.pack()
        button_institutions = Button(main_menu_frame, text="Institutions",
                                     command=lambda: self.show_frame('Institutions'))
        button_institutions.pack()
        self.frames.update({'Menu': main_menu_frame})

    def add_persons_frame(self):
        persons_frame = Frame(self, bg='#555555')
        # button = Button(persons_frame, text="You're in Persons")
        # button.pack()
        self.frames['Persons List'] = None
        self.frames.update({'Persons': persons_frame})

    def update_persons_frame(self, persons):
        if self.frames['Persons List'] is not None:
            print("Replacing it!")
            self.frames['Persons List'].pack_forget()
            self.frames['Persons List'].destroy()

        self.frames['Persons List'] = Frame(self.frames['Persons'])
        self.frames['Persons List'].pack(fill=X)

        persons = self.controller.get_persons()

        for i in range(len(persons)):
            frame = self.add_person_frame(persons[i], self.frames['Persons List'], i)
            frame.pack(fill=X, expand=True)
            # label = persons[i]['fName'] + " " + persons[i]['lName']
            # new_button = Button(self.frames['Persons'], text=label)
            # new_button.grid(column=0, row=i)

    def add_person_frame(self, person, parent, index):
        # label = person['fName'] + " " + person['lName']
        # new_button = Button(parent, text=label)
        if index % 2 == 0:
            color = '#3F3F3F'
        else:
            color = '#303030'
        meta_frame = Frame(parent)
        frame = self.generate_person_frame_small(person, parent, index, meta_frame, None, color)
        return meta_frame

    def generate_person_frame_small(self, person, parent, index, meta_frame, old_frame, color):
        if old_frame is not None:
            old_frame.pack_forget()
        frame = Frame(meta_frame, bg=color)
        frame.columnconfigure(1, weight=1)
        frame.columnconfigure(2, weight=2)
        frame.columnconfigure(3, weight=1)
        name_text = person['fName'] + ' ' + person['lName']
        name_label = Label(frame, text=name_text, padx=10, pady=10, bg=color, fg="#DEDEDE")
        name_label.grid(column=1, row=0)
        expand_button = Button(frame, text="More", padx=10,
                               command=lambda: self.generate_person_frame_large(
                                   person, parent, index, meta_frame, frame, color))
        expand_button.grid(column=3, row=0)
        # new_button.grid(column=0, row=index)
        frame.pack(fill=X, expand=True)
        return frame

    def generate_person_frame_large(self, person, parent, index, meta_frame, old_frame, color):
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
        name_text = person['fName'] + ' ' + person['lName']
        name_label = Label(frame, text=name_text, padx=10, pady=60, bg=color, fg="#DEDEDE")
        name_label.grid(column=1, row=0)
        expand_button = Button(frame, text="Less", padx=10,
                               command=lambda: self.generate_person_frame_small(
                                   person, parent, index, meta_frame, frame, color))
        expand_button.grid(column=3, row=0)
        # new_button.grid(column=0, row=index)
        frame.pack(fill=X, expand=True)

    def add_institutions_frame(self):
        institutions_frame = Frame(self, bg='#555555')
        button = Button(institutions_frame, text='You\'re in Institutions')
        button.pack()
        self.frames.update({'Institutions': institutions_frame})

    def add_productions_frame(self):
        productions_frame = Frame(self, bg='#555555')
        # button = Button(productions_frame, text='You\'re in Productions')
        # button.pack()
        self.frames['Productions List'] = None
        self.frames.update({'Productions': productions_frame})

    def update_productions_frame(self, persons):
        if self.frames['Productions List'] is not None:
            print("Replacing it!")
            self.frames['Productions List'].pack_forget()
            self.frames['Productions List'].destroy()

        self.frames['Productions List'] = Frame(self.frames['Productions'])
        self.frames['Productions List'].pack(fill=X)

        productions = self.controller.get_productions()

        for i in range(len(productions)):
            frame = self.add_production_frame(productions[i], self.frames['Productions List'], i)
            frame.pack(fill=X, expand=True)
            # label = persons[i]['fName'] + " " + persons[i]['lName']
            # new_button = Button(self.frames['Persons'], text=label)
            # new_button.grid(column=0, row=i)

    def add_production_frame(self, person, parent, index):
        # label = person['fName'] + " " + person['lName']
        # new_button = Button(parent, text=label)
        if index % 2 == 0:
            color = '#3F3F3F'
        else:
            color = '#303030'
        meta_frame = Frame(parent)
        frame = self.generate_production_frame_small(person, parent, index, meta_frame, None, color)
        return meta_frame

    def generate_production_frame_small(self, production, parent, index, meta_frame, old_frame, color):
        if old_frame is not None:
            old_frame.pack_forget()
        frame = Frame(meta_frame, bg=color)
        frame.columnconfigure(1, weight=1)
        frame.columnconfigure(2, weight=2)
        frame.columnconfigure(3, weight=1)
        name_text = production['name']
        name_label = Label(frame, text=name_text, padx=10, pady=10, bg=color, fg='#DEDEDE')
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
        name_label = Label(frame, text=name_text, padx=10, pady=60, bg=color, fg='#DEDEDE')
        name_label.grid(column=1, row=0)
        expand_button = Button(frame, text='Less', padx=10,
                               command=lambda: self.generate_production_frame_small(
                                   production, parent, index, meta_frame, frame, color))
        expand_button.grid(column=3, row=0)
        # new_button.grid(column=0, row=index)
        frame.pack(fill=X, expand=True)

    def add_events_frame(self):
        events_frame = Frame(self, bg='#555555')
        button = Button(events_frame, text='You\'re in Events')
        button.pack()
        self.frames.update({'Events': events_frame})

    def show_frame(self, name):
        print('Window switching to frame "' + name + '".')
        self.controller.switch_to(name)
        if self.current_frame is not None:
            self.current_frame.pack_forget()
        frame = self.frames[name]
        self.current_frame = frame
        frame.pack(fill=BOTH, expand=True)
        print('Window switched.')


def show_window(controller):
    root = Tk()
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
