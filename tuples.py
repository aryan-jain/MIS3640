def sumall(*nums):
    result = 0
    for i in nums:
        result += i
    return result


#testing
print(sumall(1,2,3,4,5))
print(sumall(1,2,3,4,5,6,7,8,9,10))