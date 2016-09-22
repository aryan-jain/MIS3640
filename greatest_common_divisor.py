'''
#Using Euclid's worked example
def gcd(x,y):
    if(x%y == 0):
        return y
    else:
        for i in range(1,y):
            if(x-(i*y) < y):
                return gcd(y, (x-(i*y)))
'''
#Both above and below methods work. The one below is easier to read but the one above works according to Euclid's example.

def gcd(x,y):
    if(y == 0):
        return x
    else:
        return gcd(y, x%y)

print(gcd(1071, 462))
print(gcd(97,13))