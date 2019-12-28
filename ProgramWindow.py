from tkinter import *

class Window(Frame):

    def __init__(self, master, controller):
        Frame.__init__(self, master)
        self.master = master
        self.controller = controller
        self.frames = {}
        self.current_frame = None
        self.Menu = None

        self.pack(side="top", fill="both", expand=True)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.add_menu_bar()

        self.add_context_drop()

        self.add_menu_frame()
        self.add_persons_frame()
        self.add_institutions_frame()

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
        main_menu_frame = Frame(self, bg="#DEDEDE")
        button_persons = Button(main_menu_frame, text="Persons", command=lambda: self.show_frame('Persons'))
        button_persons.pack()
        button_institutions = Button(main_menu_frame, text="Institutions",
                                     command=lambda: self.show_frame('Institutions'))
        button_institutions.pack()
        self.frames.update({'Menu': main_menu_frame})

    def add_persons_frame(self):
        persons_frame = Frame(self, bg="#CCCCCC")
        button = Button(persons_frame, text="You're in Persons")
        button.pack()
        self.frames.update({'Persons': persons_frame})

    def add_institutions_frame(self):
        institutions_frame = Frame(self, bg="#EEAAAA")
        button = Button(institutions_frame, text="You're in Institutions")
        button.pack()
        self.frames.update({'Institutions': institutions_frame})

    def show_frame(self, name):
        print('Switching to frame "' + name + '".')
        if self.current_frame is not None:
            self.current_frame.pack_forget()
        frame = self.frames[name]
        self.current_frame = frame
        frame.pack(fill=BOTH, expand=True)


def show_window(controller):
    root = Tk()
    app = Window(root, controller)

    root.wm_title("OffBook Lite")
    # root.geometry("320x200");

    # root.attributes('-fullscreen', True)  #fullscreens the window

    # w, h = root.winfo_screenwidth(), root.winfo_screenheight()  #resizes window to screen size
    # root.geometry("%dx%d+0+0" % (w, h))

    root.state('zoomed')    # maximizes window

    root.mainloop()  # show window

    return root
