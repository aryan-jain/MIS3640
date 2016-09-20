def bmi():
    type = input("USA or Metric?")
    height = float(input("Height (inches only)?  "))
    weight = int(input("Weight (lbs only)?  "))

    if(type == "USA" or type == "usa"):
        x = 703*(weight/(height**2))

    elif(type == "Metric" or type == "metric"):
        x = weight/(height**2)
   
    if x < 18.5:
        print('BMI: ', x)
        print('You are underweight.')
    #elif x in range(18.5, 24.9):
    elif x > 18.5 and x <= 25:
        print('BMI: ', x)
        print('You are normal weight')
    #elif x in range(25, 29.9):
    elif x < 25 and x <= 30:
        print('BMI: ', x)
        print('You are overweight')
    else:
        print('BMI: ', x)
        print('You are suffering obesity.')

bmi()
    




input()