#module imports
import math

#function definition
def quadratic(a, b, c):
    det = (b**2) - (4*a*c)
    if det >= 0:
        x1 = (-b - math.sqrt(det))/(2*a)
        x2 = (-b + math.sqrt(det))/(2*a)   
        return x1, x2
    else:
        print("This expression has no real roots.")

#testing
print(quadratic(3, 4, 5))  #This quadratic has no defined roots and should, therefore, return an error message.
print(quadratic(1,4,2)) #This quadratic does have real roots and should, therefore, return the two roots.
print(quadratic(3,6,3)) #This quadratic has repeating roots and should, therefore, return the same number twice.


input()