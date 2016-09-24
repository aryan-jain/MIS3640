sum = 0 

#for i in range(11):  #the range function always initiates at 0, therefore, we use range(11) instead of range(10)
#    sum = sum+i



for i in range(1001):
    if(i%2 == 1):
        print(i)
        sum += i   #same as sum = sum + i

print(sum)



iteration = 0
count = 0
while iteration < 5:
    # the variable 'letter' in the loop stands for every 
    # character, including spaces and commas!
    for letter in "hello, world": 
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1 