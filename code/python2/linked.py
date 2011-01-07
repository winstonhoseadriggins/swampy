def link(first, rest=tuple()):
    return first, rest

def first(t):
    return t[0]

def rest(t):
    return t[1]

t = link(1, link(2, link (3)))

print repr(t)

