import re


def find_person(beginning, persons, production_id=None):
    """Find all persons from a provided list that match a provided name."""
    matching_persons = []
    exp = re.compile(beginning, re.I)
    for person in persons:
        if exp.match(person['fName']) or exp.match(person['lName']):
            matching_persons.append(person)
    return matching_persons


def find_production(text, productions, institution_id=None):
    """Find all productions form a provided list that matches provided text to a name or description."""
    matching_productions = []
    exp = re.compile(text, re.I)
    for production in productions:
        if exp.match(production['name']) or exp.match(production['description']):
            matching_productions.append(production)
    return matching_productions
