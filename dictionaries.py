def histogram(s):
    '''
    Takes a string input and returns a dictionary that 
    maps each character in the string to the number of
    times it appears in the string.
    Input: 'Bookkeeper'
    Output: {'o': 2, 'r': 1, 'k': 2, 'e': 3, 'p': 1, 'B': 1}
    '''
    d = dict()
    for c in s:
        d[c] = d.get(c,0)+1
    return d

def print_hist(h):
    '''
    Prints the dictionary created by the function histogram()
    in a tabular, sorted format
    '''
    for c in sorted(h):
        print(c, h[c])

def reverse_lookup(d, v):
    '''
    This function takes 2 inputs:
    d - Dictionary
    v - Value
    and returns the key in 'd' that appears 'v'
    number of times.
    '''
    for k in d:
        if d[k] == v:
            return k
    raise LookupError('Value does not occur in dictionary.')


#testing
h = histogram('Bookkeeper')
print(h)

print_hist(h)

print(reverse_lookup(h,2))
#print(reverse_lookup(h,4))     #this line should return a lookup error 
