def histogram(s):
    d = dict()
    for c in s:
        d[c] = s.get(c,0)
    return d

h = histogram('Bookkeeper')
print(h)