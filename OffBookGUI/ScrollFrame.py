from tkinter import *


class ScrollFrame(Frame):
    def __init__(self, view, holder_frame=None):
        super(ScrollFrame, self).__init__(holder_frame, background='#0000FF')
        self.view = view
        self.canvas = Canvas(self, background='#FF0000')
        self.child_frame = Frame(self.canvas, background='#00FF00')
        self.scrollbar = Scrollbar(self, orient="vertical")
        self.scrollbar.pack(side='right', fill='y')
        self.items = []

    def add(self, item):
        self.items.append(item)
        item.config(master=self.child_frame)

    def get_canvas(self):
        return self.canvas

    def reset_child(self):
        self.items = []
        self.child_frame.pack_forget()
        self.child_frame.destroy()
        self.child_frame = Frame(self.canvas)

