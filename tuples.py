def sumall(*nums):
    result = 0
    for i in nums:
        result += i
    return result


#testing
print(sumall(1,2,3,4,5))
print(sumall(1,2,3,4,5,6,7,8,9,10))

def most_frequent(word):
    from operator import itemgetter
    d = dict()
    for c in word:
        d[c] = d.get(c,0)+1
    a = list(d.items())
    for x,y in sorted(a, key=itemgetter(1), reverse=True):
        print(x, y)

#testing
most_frequent('bookkeeper')