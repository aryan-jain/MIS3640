def my_abs(x):
    if isinstance(x, int) or isinstance(x, float):
        if x >= 0:
            return x
        else:
            return (-x)
    else:
        print("This data type is not supported by the my_abs function.")

#a = my_abs(-100)
#b = my_abs(-4.234)
#c = my_abs(13)
#d = my_abs(0)
e = my_abs('A')
#print(a, b, c, d)