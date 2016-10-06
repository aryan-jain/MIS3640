"""
Four suspects; one of them is a thief. In interrogation
    John said: I am not the thief.
    Paul said: George is the thief.
    George said: It must be Ringo.
    Ringo said: George is lying.

Among them, three were telling the truth while one was lying.
Could you find out who is the thief?

"""
for thief in ['John', 'Paul', 'George', 'Ringo']:
    if (thief is not 'John') + (thief is 'George') + (thief is 'Ringo') + (thief is not 'Ringo') == 3:
        print(thief)