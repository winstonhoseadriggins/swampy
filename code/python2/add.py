def add(t):
    total = 0
    for x in t:
        total += x
    return total

def capitalize(t):
    res = []
    for s in t:
        res.append(s.upper())
    return res

def only_upper(t):
    res = []
    for s in t:
        if s.isupper():
            res.append(s)
    return res

t = range(10)

t = ['eric', 'michael', 'graham', 'john', 'terry']
t2 = capitalize(t)

t3 = only_upper(t2)

print t3
