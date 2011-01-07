def histogram(s):
    d = {}
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] = d[c]+1
    return d

def print_hist(h):
    for c in h:
        print c, h[c]

def reverse_lookup(d, v):
    for k in d:
        if d[k] == v:
            return k
    raise ValueError

def invert_dict(d):
    inv = {}
    for key in d:
        val = d[key]
        if val not in inv:
            inv[val] = [key]
        else:
            inv[val].append(key)
    return inv


import Lumpy
lumpy = Lumpy.Lumpy()

hist = histogram('parrot')
inv = invert_dict(hist)

lumpy.object_diagram()


print inv

print inv[1]

print inv[2]
