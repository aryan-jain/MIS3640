import turtle
import math
from Turtle import polygon, polyline, circle, arc

# Excercise 3 - Problem 1.1
def triangle_circle(t):
    t.speed(9)
    circle(t,100)
    t.lt(90)
    t.pu()
    t.fd(100)
    t.pd()
    for i in range(4):
        t.seth((i*90)-30)
        polygon(t,3,100)
    for i in range(4):
        t.seth(i*90-30)
        t.pu()
        t.fd(50)
        t.pd()
        circle(t,math.sqrt((50**2)/3))
        t.pd()
        t.bk(50)

    turtle.mainloop()


#Exercise 3 - Problem 1.2
def flower(t):
    circle(t,100)
    for i in range(3):
        t.lt(360/6)
        arc(t,100,360/3)
        t.lt(360/6)
    t.pu()
    arc(t,100,180)
    t.pd()
    for i in range(3):
        t.lt(360/6)
        arc(t,100,360/3)
        t.lt(360/6)

    turtle.mainloop()


#Exercise 3 - Problem 1.3
def yinyang(t):
    t.speed(9)
    circle(t,120)
    t.pu()
    arc(t,60,180)
    t.pd()
    arc(t,60,180)
    t.pu()
    t.lt(90)
    t.fd(120)
    t.rt(90)
    t.pd()
    arc(t,60,180)
    t.pu()
    t.lt(90)
    t.fd(40)
    t.rt(90)
    t.pd()
    circle(t,120/6)
    t.pu()
    t.lt(90)
    t.fd(120)
    t.rt(90)
    t.pd()
    circle(t,120/6)

    turtle.mainloop()


#testing
aryan = turtle.Turtle()

#triangle_circle(aryan)

#flower(aryan)

#yinyang(aryan)

