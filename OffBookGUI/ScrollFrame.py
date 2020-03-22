from tkinter import *


class ScrollFrame(Frame):
    def __init__(self, view, holder_frame=None):
        super(ScrollFrame, self).__init__(holder_frame, background='#0000FF')
        self.view = view
        self.scrollbar = Scrollbar(self, orient='vertical')
        self.canvas = Canvas(self, background='#00FF00')
        self.canvas.config(yscrollcommand=self.scrollbar.set, scrollregion=self.canvas.bbox(ALL))
        # self.child_frame = Frame(self.canvas, background='#FF0000', height=10000, width=1000)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.scrollbar.config(command=self.canvas.yview)
        # self.child_frame.pack(padx=10, pady=10)
        self.canvas.pack(fill=BOTH, padx=10, pady=10)
        self.items = []
        self.canvas.bind_all('<MouseWheel>', self._on_mousewheel)

    def add(self, item):
        self.items.append(item)
        item.config(master=self.child_frame)

    def get_canvas(self):
        return self.canvas

    def reset_child(self):
        self.items = []
        self.child_frame.pack_forget()
        self.child_frame.destroy()
        # self.child_frame = Frame(self.canvas, background='#00FF00')

    def set_bbox(self):
        print('Bounding box',  self.canvas.bbox(ALL))
        # self.canvas.config(scrollregion=self.canvas.bbox(ALL))
        self.canvas.config(scrollregion=(0, 0, 10000, 10000))

    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), 'units')
