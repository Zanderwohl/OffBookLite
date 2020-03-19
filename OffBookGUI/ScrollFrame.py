from tkinter import *


class ScrollFrame(Frame):
    def __init__(self, view, holder_frame=None):
        super(ScrollFrame, self).__init__(holder_frame, background='#0000FF')
        self.view = view
        self.canvas = Canvas(self, background='#FF0000')
        self.child_frame = Frame(self.canvas, background='#00FF00')
        self.scrollbar = Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side='right', fill='y')
        self.canvas.pack(side='left', fill=BOTH, expand=True)
        self.child_frame.pack(fill=BOTH, expand=True)
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
