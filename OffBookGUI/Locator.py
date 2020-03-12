from tkinter.ttk import *


class Locator(Label):
    def __init__(self, root, theme):
        super(Locator, self).__init__(root, background=theme['Widget'], foreground=theme['Text'])

    def update(self, institution, production, event):
        if institution is None:
            institution = {'name': 'None'}
        if production is None:
            production = {'name': 'None'}
        if event is None:
            event = {'name': 'None', 'startTime': ''}
        text = institution['name'] + '>' + production['name'] + '>' + event['startTime'] + ' ' + event['name']
        super().config(text=text)
