import random
import dbm
import os

def open_db():
    ROSTER = ("Beshansky",
            "Collins",
            "Fischer",
            "Giovanucci",
            "Jain",
            "Kim",
            "Lauture",
            "Lee",
            "Maddox",
            "Martinez",
            "Mendez",
            "Oh",
            "Petrone",
            "Posada",
            "Rule",
            "Schilb",
            "Tariq",
            "Wang",
            "Wolf")
    if not os.path.exists('db_roster.dir'):
        db = dbm.open('db_roster', 'c')
        for student in ROSTER:
            db[student]='0'
        return db
    else:
        db = dbm.open('db_roster', 'c')
        return db
def call(roster):
    """
    Among the names that are called least times,
    return one name from the names that are called least times
    roster: a dict of names and integers
    """
    #print(random.sample(roster, 3))
    values = [int(x[1]) for x in roster.items()]
    minimum = min(values)

    temp = dict()
    for key, value in roster.items():
        if int(value) == minimum:
            temp[key] = value

    student = random.choice(list(temp.keys()))

    visits = int(roster[student]) + 1

    roster[student] = str(visits)

    return student


# Testing

roster = open_db()
print(roster.items())       #Check the current number of visits of each student
print(call(roster))         #Call a random student who has appeared the minimum number of times before
print(roster.items())       #Check if the database updates the student's number of visits