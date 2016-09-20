age = 11

if age >= 21:
    print('Your age is '+str(age)+'.')
    print('Yes, you can!')
elif age >= 12:
    print('Your age is ', age,'.')
    print('No, you cannot. You are just a teenager!')
else:
    print('Your age is %d.' % age)
    print('No, you cannot. You are just a kid!')

input()