import os

themes_directory = 'themes'


def parse_theme(file_path):
    if not len(file_path.split('.')) == 2:
        file_path = file_path.lower() + '.config'
    theme_file = open(themes_directory + '/' + file_path, "r")
    theme = {}
    for pair in theme_file:
        key, value = pair.split("=")
        theme[key] = value.strip()  # strip() removes newlines.
    theme_file.close()
    return theme


def construct_themes():
    if not os.path.exists(themes_directory):
        os.mkdir(themes_directory)
    theme_files = os.listdir(path=themes_directory)
    themes = {}
    for file in theme_files:
        new_theme = parse_theme(file)
        themes[new_theme['Name']] = new_theme
    return themes


print(construct_themes())
