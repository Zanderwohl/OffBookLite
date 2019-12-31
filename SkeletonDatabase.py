
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
        "fName": "Emilie",
        "lName": "Swonger",
        "institutionId": 2
    }, {
        "id": 4,
        "fName": "Eulalia",
        "lName": "Lowry",
        "institutionId": 2
    }, {
        "id": 7,
        "fName": "Seven",
        "lName": "The Seven Boy",
        "institutionId": 2
    }
    ]
    return query


def get_persons(institutionId):
    unfiltered = persons()
    query = []
    for person in unfiltered:
        if person.get("institutionId") == institutionId:
            query.append(person)
    return query


def get_productions(admin=False, productionId=None):
    query = [
        {
            "id": 23,
            "name": "Dark Star",
            "description": "The anti-musical.",
            "institutionId": 1,
            "startDate": "2019-01-01 12:00:00 AM",
            "endDate": "2019-01-01 12:10:00 AM",
            "deleted": 1
        },
        {
            "id": 22,
            "name": "Noises Off!",
            "description": "Spring 18/19 show.",
            "institutionId": 1,
            "startDate": "2018-01-01 12:00:00 AMM",
            "endDate": "2021-01-01 12:10:00 AM",
            "deleted": 0
        },
        {
            "id": 21,
            "name": "The Crucible",
            "description": "The 18/19 classic drama.",
            "institutionId": 1,
            "startDate": "2019-01-01 7:00:00 PM",
            "endDate": "2019-05-09 7:00:00 PM",
            "deleted": 0
        },
        {
            "id": 20,
            "name": "Department Events",
            "description": "General events shared throughout the department.",
            "institutionId": 1,
            "startDate": "2000-12-31 7:00:00 PM",
            "endDate": "2020-12-31 12:00:00 AM",
            "deleted": 0
        },
        {
            "id": 19,
            "name": "Fantastic Mr. Fox",
            "description": "The 18/19 children's show.",
            "institutionId": 1,
            "startDate": "2019-04-21 1:00:00 AM",
            "endDate": "2019-05-11 1:00:00 AM",
            "deleted": 0
        }
    ]
    return query

