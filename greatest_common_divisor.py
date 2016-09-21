def gcd(x,y):
    if(x%y == 0):
        return y
    else:
        for i in range(1,y):
            if(x-(i*y) < y):
                return gcd(y, (x-(i*y)))

print(gcd(1071, 462))
print(gcd(97,13))