def sumall(*nums):
    result = 0
    for i in nums:
        result += i
    return result


#testing
print(sumall(1,2,3,4,5))
print(sumall(1,2,3,4,5,6,7,8,9,10))

'''
def most_frequent(word):
    from operator import itemgetter
    d = dict()
    for c in word:
        d[c] = d.get(c,0)+1
    a = list(d.items())
    for x,y in sorted(a, key=itemgetter(1), reverse=True):
        print(x, y)
'''

def most_frequent(word):
    from time import sleep
    result = dict()
    print('Please wait. Parsing through textfile. This may take a while.')
    print('Loading...', end='')
    sleep(1)
    print('.', end="")
    sleep(1)
    print('.', end="")
    sleep(1)
    print('.', end="")
    for line in word:
        s = line.strip()
        x = list(s)
        for i in x:
            if i not in result:
                result[i] = 1
            else:
                result[i] += 1
    final = list(result.items())
    final = sorted(final, key=lambda tup:(tup[1],tup[0]), reverse=True)
    sleep(1)
    print('.', end="")
    sleep(1)
    print('.', end="         ")
    print('DONE!')
    sleep(1)
    for a,b in final:
        print('%s: %d' %(a,b))



#testing
most_frequent('bookkeeper')

eng = open('blackcat.txt')

# https://docs.python.org/3/library/functions.html#repr

most_frequent(eng)