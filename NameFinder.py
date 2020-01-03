import re


def find(beginning, persons):
    matching_persons = []
    exp = re.compile(beginning, re.I)
    for person in persons:
        if exp.match(person['fName']) or exp.match(person['lName']):
            matching_persons.append(person)
    return matching_persons
