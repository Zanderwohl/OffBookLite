from tkinter import *


class ScrollFrame(Frame):
    def __init__(self, view, holder_frame=None):
        super(ScrollFrame, self).__init__(holder_frame)
        self.view = view
        self.canvas = Canvas(self)
        self.child_frame = Frame(self.canvas)
        self.scrollbar = Scrollbar(holder_frame, orient="vertical", command=self.canvas.yview)
        self.canvas.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side='right', fill='y')
        self.canvas.pack(side='left', fill='x')
        self.child_frame.pack()
        self.items = []

    def add(self, item):
        self.items.append(item)
        item.config(master=self.child_frame)

    def get_canvas(self):
        return self.canvas

    def reset_child(self):
        # for item in self.items:
        #    item.pack_forget()
        #    item.destroy()
        self.items = []
        self.child_frame.pack_forget()
        self.child_frame.destroy()
        self.child_frame = Frame(self.canvas)
