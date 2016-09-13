def my_abs(x):
    if x >= 0:
        return x
    else:
        return (-x)

a = my_abs(-100)
b = my_abs(-4.234)
c = my_abs(13)

print(a, b, c)