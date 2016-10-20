import random

ROSTER = {"Beshansky": 0,
          "Collins": 0,
          "Fischer": 1,
          "Giovanucci": 0,
          "Jain": 0,
          "Kim": 0,
          "Lauture": 0,
          "Lee": 0,
          "Maddox": 0,
          "Martinez": 0,
          "Mendez": 0,
          "Oh": 0,
          "Petrone": 1,
          "Posada": 0,
          "Rule": 1,
          "Schilb": 0,
          "Tariq": 0,
          "Wang": 0,
          "Wolf": 0}


def call(roster):
    """
    Among the names that are called least times,
    return one name from the names that are called least times
    roster: a dict of names and integers
    """
    #print(random.sample(roster, 3))
    d = dict()
    for key, value in roster.items():
        if value == min(roster.values()):
            d[key] = value
    return random.choice(list(d.keys()))

print(call(ROSTER))