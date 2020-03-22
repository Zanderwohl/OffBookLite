import operator
from tkinter import *


class ScrollFrame(Frame):
    def __init__(self, view, theme, holder_frame=None):
        # Note to self: it's possible the items on the canvas are not attached to the canvas surface somehow, and
        # therefore not scrolling.
        # Or the canvas size
        super(ScrollFrame, self).__init__(holder_frame, background=theme['Background'])
        self.view = view
        self.scrollbar = Scrollbar(self, orient='vertical')
        self.canvas = Canvas(self, background=theme['Background'])
        self.child_frame = Frame(self.canvas, background=theme['Background'])
        self.child_frame.bind('<Configure>', lambda e: self.canvas.configure(scrollregion=self.canvas.bbox(ALL)))
        # self.child_frame.bind('<Configure>', lambda e: self.canvas.configure(scrollregion=tuple(map(operator.sub, (0, 0, self.winfo_width(), self.winfo_height()), self.canvas.bbox(ALL)))))
        self.canvas.config(yscrollcommand=self.scrollbar.set, borderwidth=0)  # TODO: remove canvas' white border
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.scrollbar.config(command=self.canvas.yview)
        self.canvas.pack(fill=BOTH, expand=True)
        self.child_frame.pack(fill=BOTH, expand=True)
        self.canvas.bind_all('<MouseWheel>', self._on_mousewheel)
        self.canvas_window = self.canvas.create_window((0, 0), window=self.child_frame, anchor='nw')
        self.canvas.bind('<Configure>', self._on_frame_change)

    def add(self, item):
        self.items.append(item)
        item.config(master=self.child_frame)

    def get_canvas(self):
        return self.canvas

    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), 'units')

    def _on_frame_change(self, event):
        canvas_width = event.width
        self.canvas.itemconfig(self.canvas_window, width=canvas_width)

