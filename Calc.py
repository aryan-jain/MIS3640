#arithmetic operator testing

print(46+37+38)

print(145/12)

print(7*11)

print(145%12)

print(12-112)

#age calculation

print('My age is:')
print(2016-1995)

#exponent test

print(3**10)

#HOMEWORK
#1. Volume of a sphere
r = 5
vol = (4/3)*3.1415926*(r**3)
print('The volume of a sphere with radius %d is %d' % (r,vol))

#2. Bookstores
cp = 24.95
discount = 0.4
ship1 = 3
ship = 0.75
n = 60
tcost = n*(cp*(1-discount)) + ship1 + (n-1)*ship

#3. Workout
print('I will arrive home at %d:%2d:%0d' % (7,45,0))

#4. Average grade
increase = (89-82)/82
increase = increase * 100
print('The average increased by %.2f %%' % increase)

input()