from tkinter import *


class Window(Frame):

    def __init__(self, master, controller):
        Frame.__init__(self, master)
        self.master = master
        self.controller = controller

        self.pack(fill=BOTH, expand=1)

        exit_button = Button(self, text="Exit", command=self.v_exit)
        exit_button.place(x=0, y=0)

        self.add_menu_bar()
        # self.add_file_drop()
        # self.add_edit_drop()
        # self.add_calc_drop()

        self.add_context_drop()

    def add_menu_bar(self):
        self.menu = Menu(self.master)
        self.master.config(menu=self.menu)

    def add_context_drop(self):
        context_menu = Menu(self.menu)
        context_menu.add_command(label="Persons", command=self.persons_context())
        context_menu.add_command(label="Institutions", command=self.institutions_context())
        self.menu.add_cascade(label="Context", menu=context_menu)

    def add_file_drop(self):
        file_menu = Menu(self.menu)
        file_menu.add_command(label="New")
        file_menu.add_command(label="Open")
        file_menu.add_command(label="Save")
        file_menu.add_command(label="Save as...")
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.v_exit);
        self.menu.add_cascade(label="File", menu=file_menu)

    def add_edit_drop(self):
        edit_menu = Menu(self.menu)
        edit_menu.add_command(label="Duplicate")
        edit_menu.add_command(label="Time")
        self.menu.add_cascade(label="Edit", menu=edit_menu)

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

    def persons_context(self):
        print('Switch to persons context')

    def institutions_context(self):
        print('Switch to institutions context')


def show_window(controller):
    root = Tk()
    app = Window(root, controller)

    root.wm_title("OffBook Lite")
    root.geometry("320x200");

    root.mainloop()  # show window

    return root
