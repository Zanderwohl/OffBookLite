import random
from time import strftime
from tkinter.ttk import *


class QOTD(Label):
    def __init__(self, root, theme, quotes):
        super(QOTD, self).__init__(root, background=theme['Widget'], foreground=theme['Text'])
        self.generate_quote(quotes)

    def generate_quote(self, quotes):
        time = str(strftime('%Y')) + str(strftime('%m')) + str(strftime('%d'))
        random.seed(int(time))
        index = random.randint(0, len(quotes) - 1)
        quote = quotes[str(index)]
        content = quote['quote'] + '\n\t-' + quote['author']
        super().config(text=content)
