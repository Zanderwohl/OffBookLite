import os
from pandas import *
import numpy as np


class Theme:
    def __init__(self):
        theme_files = os.listdir(path='themes/')
        self.themes = []
        for file in theme_files:
            theme_csv = read_csv('themes/' + file)
            theme_csv = np.array(theme_csv)
            theme = {}
            for key in theme_csv:
                theme[key[0]] = key[1]
            self.themes.append(theme)
            for key in theme:
                print(key + ":" + theme[key])

    def get_value(self, theme, key):
        return self.themes
    # TODO: Write this function


theme_manager = Theme()
