import math
'''
x = float(input())

if x > 0:
    y = math.log(x)
else:
    y = float('nan') # a special floating-point value that represents “Not a Number”. 
print(y)

y = math.log(x) if x > 0 else float('nan')

print(y)
'''

def capitalize_all(t):
    res = []
    for s in t: 
        res.append(s.capitalize())
    return res

a = 'babson'
print(capitalize_all(a))

def capitalize_all2(t):
    return [s.capitalize() for s in t]

a = 'babson'
print(capitalize_all2(a))

g = (x * x for x in range(5))
g