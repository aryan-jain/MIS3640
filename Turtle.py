import turtle
import math

aryan = turtle.Turtle()
'''
def square(t):
    for i in range(4):
        t.fd(100)
        t.lt(90)
    print(t)

square(aryan)
'''

def square(t,length):
    for i in range(4):
        t.fd(length)
        t.lt(90)
    print(t)

#square(aryan,200)

'''def polygon(t,length,n):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)
    print(t)'''

#polygon(aryan,1,360)

'''def circle(t, r):
    circumference = 2 * math.pi * r
    n = int(circumference / 3) + 1
    length = circumference // n
    t.speed(0)
    polygon(t, length, n)'''

#circle(aryan, 100)
'''
def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    
    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)
'''
#arc(aryan, 100, 180)

def polyline(t, n, length, angle):
    """Draws n line segments with the given length and
    angle (in degrees) between them.  t is a turtle.
    """ 
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def polygon(t, n, length):
    angle = 360.0 / n
    polyline(t, n, length, angle)

def arc(t, r, angle):
    t.speed(9)
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)

def circle(t,r):
    arc(t,r,360)



#testing
#square(aryan,200)
#arc(aryan, 100, 180)
#polygon(aryan,6,100)
#circle(aryan, 100)
