from tkinter import *


class Window(Frame):

    def __init__(self, master, controller):
        Frame.__init__(self, master)
        self.master = master
        self.controller = controller
        self.frames = {}

        self.pack(side="top", fill="both", expand=True)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # exit_button = Button(self, text="Exit", command=self.v_exit)
        # exit_button.place(x=0, y=0)

        self.add_menu_bar()
        # self.add_file_drop()
        # self.add_edit_drop()
        # self.add_calc_drop()

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
        # User exit (0).
        # SystemC.exit(0)

    def add_menu_frame(self):
        main_menu_frame = Frame(self, bg="#DEDEDE")
        main_menu_frame.pack(expand=True, fill='both')
        self.frames.update({'Menu': main_menu_frame})

    def show_menu_frame(self):
        print('Switching to main menu.')
        self.show_frame('Menu')

    def add_persons_frame(self):
        persons_frame = Frame(self, bg="#CCCCCC")
        persons_frame.pack(fill=BOTH, expand=True)
        button = Button(persons_frame, text="Persons")
        button.pack()
        self.frames.update({'Persons': persons_frame})

    def show_persons_frame(self):
        print('Switching to persons.')
        self.show_frame('Persons')

    def add_institutions_frame(self):
        institutions_frame = Frame(self, bg="#EEAAAA")
        institutions_frame.pack(fill=BOTH, expand=True)
        button = Button(institutions_frame, text="Institutions")
        button.pack()
        self.frames.update({'Institutions': institutions_frame})

    def show_institutions_frame(self):
        print('Switching to institutions.')
        self.show_frame('Institutions')

    def show_frame(self, name):
        for key, value in self.frames.items():
            value.pack_forget()
        frame = self.frames[name]
        frame.pack(fill=BOTH, expand=True)
        # frame.tkraise()


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
