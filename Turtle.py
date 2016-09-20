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

def polygon(t,length,n):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)
    print(t)

#polygon(aryan,1,360)

def circle(t,r):
    length = 1
    n = 1
    length*n = 2*math.pi*r
    