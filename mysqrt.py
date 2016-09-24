from random import randint

def mysqrt(a):
    if(a<0):
        print('Negative numbers do not have real roots!')
    else:
        x = randint(1,a)
        #print(x)
        while True:
            y = (x+(a/x))/2
            #print(y)
            if (abs(x-y) < 0.00000001):
                break
            x = y
        return x


#mysqrt(16)