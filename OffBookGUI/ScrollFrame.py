from tkinter import *


class ScrollFrame(Frame):
    def __init__(self, view, holder_frame=None):
        # Note to self: it's possible the items on the canvas are not attached to the canvas surface somehow, and
        # therefore not scrolling.
        # Or the canvas size
        super(ScrollFrame, self).__init__(holder_frame, background='#0000FF')
        self.view = view
        self.scrollbar = Scrollbar(self, orient='vertical')
        self.canvas = Canvas(self, background='#00FF00', height=10000, width=10000)
        self.child_frame = Frame(self.canvas, background='#FF0000')
                                 #, height=10000, width=1000)
        self.child_frame.bind('<Configure>', lambda e: self.canvas.configure(scrollregion=self.canvas.bbox(ALL)))
        self.canvas.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.scrollbar.config(command=self.canvas.yview)
        self.canvas.pack(fill=BOTH)
        self.child_frame.pack()
        self.canvas.bind_all('<MouseWheel>', self._on_mousewheel)
        self.canvas.create_text(100, 100, text='hello world')
        self.canvas.create_window((0, 0), window=self.child_frame, anchor='nw')

    def add(self, item):
        self.items.append(item)
        item.config(master=self.child_frame)

    def get_canvas(self):
        return self.canvas

    def set_bbox(self):
        print('Bounding box',  self.canvas.bbox(ALL))
        self.canvas.config(scrollregion=self.canvas.bbox(ALL))
        # self.canvas.config(scrollregion=(0, 0, 10000, 10000))

    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), 'units')
