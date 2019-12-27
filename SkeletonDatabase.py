
def persons():
    query = [{
        "id": 1,
        "fName": "Alexander",
        "lName": "Lowry",
        "institutionId": 3
    },{
        "id": 2,
        "fName": "Lindsey",
        "lName": "Johnson",
        "institutionId": 3
    }, {
        "id": 2,
        "fName": "Drew",
        "lName": "Littlefield",
        "institutionId": 3
    }, {
        "id": 3,
        "fName": "Emily",
        "lName": "Swonger",
        "institutionId": 2
    }, {
        "id": 4,
        "fName": "Alexander",
        "lName": "Lowry",
        "institutionId": 2
    }]
    return query


def get_persons(institutionId):
    unfiltered = persons()
    query = []
    for person in unfiltered:
        if person.get("institutionId") == institutionId:
            query.append(person)
    return query

