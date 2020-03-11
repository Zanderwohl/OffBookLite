from time import strftime
# from tkinter import *
from tkinter.ttk import *


class TimeClock(Label):
    def __init__(self, root, theme):
        super(TimeClock, self).__init__(root, background=theme['Widget'], foreground=theme['Text'])
        self.local_time()

    def local_time(self):
        time_string = strftime('%I:%M:%S %p')
        super().config(text=time_string)
        super().after(100, self.local_time)


class DateClock(Label):
    def __init__(self, root, theme):
        super(DateClock, self).__init__(root, background=theme['Widget'], foreground=theme['Text'])
        self.local_time()

    def local_time(self):
        date_string = strftime('%A\n%Y-%m-%d')
        super().config(text=date_string)
        super().after(1000, self.local_time)
