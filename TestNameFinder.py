from Model import *
import re


def test_name_finder():
    model = Model()

    expected_becky = [{'id': 14, 'fName': 'Becky', 'lName': 'Thomas', 'institutionId': 3},
                      {'id': 15, 'fName': 'Becky', 'lName': 'Anderson', 'institutionId': 3}]

    # model.query_persons()
    # true as long as the institution is 3.
    model.institution = 3
    assert(model.name_find('Ale') == [])
    assert(model.name_find('ale') == [])
    assert(model.name_find('Becky') == expected_becky)
    assert(model.name_find('Beck') == expected_becky)
    assert(model.name_find('b') == expected_becky)


test_name_finder()

