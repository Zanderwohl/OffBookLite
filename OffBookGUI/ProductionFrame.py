from tkinter import *


class ProductionFrame:
    def __init__(self, production_data, view, theme, holder_frame, color='#FFFFFF'):
        self.id = production_data.get('id') or production_data.get('productionId')
        self.name = production_data.get('name')
        self.description = production_data.get('description')
        self.start_date = production_data.get('startDate')
        self.end_date = production_data.get('endDate')
        self.expanded = False
        self.unsaved = False
        self.theme = theme
        self.color = color
        self.view = view
        self.holder_frame = holder_frame
        self.minimal_frame = self.create_minimal_frame()
        self.expanded_frame = self.create_expanded_frame()
        self.edit_frame = self.create_edit_frame()
        self.active_frame = None
        self.switch_frame(self.color, 'minimal')

    def get_frame(self, size='minimal'):
        if size == 'minimal':
            self.expanded = False
            return self.minimal_frame
        if size == 'expanded':
            self.expanded = True
            return self.expanded_frame
        if size == 'edit':
            return self.edit_frame

    def switch_frame(self, background_color, size='minimal'):
        if size == 'save':
            if self.expanded:
                size = 'expanded'
            else:
                size = 'minimal'
        if self.active_frame is not None:
            self.active_frame.pack_forget()
        new_frame = self.get_frame(size=size)
        self.active_frame = new_frame
        self.active_frame.config(bg=background_color)
        new_frame.pack(fill=X, expand=True)

    def create_minimal_frame(self):
        frame = Frame(self.holder_frame)
        frame.columnconfigure(1, weight=1)
        frame.columnconfigure(2, weight=2)
        frame.columnconfigure(3, weight=1)
        name_text = self.name
        name_label = Label(frame, text=name_text, padx=10, pady=10, bg=self.color, fg=self.theme['Text'])
        name_label.grid(column=1, row=0)
        expand_button = Button(frame, text='More', padx=10,
                               command=lambda: self.switch_frame(self.color, 'expanded'))
        expand_button.grid(column=3, row=0)
        edit_button = Button(frame, text='Edit', padx=10,
                             command=lambda: self.switch_frame(self.color, 'edit'))
        edit_button.grid(column=0, row=0)
        return frame

    def create_expanded_frame(self):
        frame = Frame(self.holder_frame)
        frame.columnconfigure(1, weight=1)
        frame.columnconfigure(2, weight=2)
        frame.columnconfigure(3, weight=1)
        frame.rowconfigure(0, weight=1)
        frame.rowconfigure(1, weight=1)
        frame.rowconfigure(2, weight=1)
        frame.rowconfigure(3, weight=1)
        frame.rowconfigure(5, weight=1)
        name_text = self.name
        name_label = Label(frame, text=name_text, padx=10, pady=60, bg=self.color, fg=self.theme['Text'])
        name_label.grid(column=1, row=0)
        expand_button = Button(frame, text='Less', padx=10,
                               command=lambda: self.switch_frame(self.color, 'minimal'))
        expand_button.grid(column=3, row=0)
        edit_button = Button(frame, text='Edit', padx=10,
                             command=lambda: self.switch_frame(self.color, 'edit'))
        edit_button.grid(column=0, row=0)
        return frame

    def create_edit_frame(self):
        frame = Frame(self.holder_frame)
        name_text = self.name
        name_label = Label(frame, text=name_text, padx=10, pady=60, fg=self.theme['Text'], bg=self.color)
        name_label.grid(column=1, row=0)
        retract_button = Button(frame, text='Save', padx=10,
                                command=lambda: self.switch_frame(self.color, 'save'))
        retract_button.grid(column=0, row=0)
        return frame

    def save(self):
        self.unsaved = False
        return {}

    def __str__(self):
        return str(self.id)


if __name__ == "__main__":
    production1 = ProductionFrame({'id': 1})
    print(production1)
    production2 = ProductionFrame({'productionId': 4})
    print(production2)
