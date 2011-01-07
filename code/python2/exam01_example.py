import Lumpy
lumpy = Lumpy.Lumpy()
lumpy.make_reference()

import copy

def make_histogram(word):
    d = {}
    for c in word:
        d[c] = d.get(c, 0) + 1
    return d

def subtract(d1, d2):
    res = copy.copy(d1)

    for key in d2:
        res[key] = d1.get(key, 0) - d2[key];

    lumpy.object_diagram()
    return res

h1 = make_histogram('aabc')
h2 = make_histogram('ab')

d = subtract(h1, h2)
print d


d = {}
d['a'] = 1
d['b'] = 2
d['c'] = 2
d['d'] = 1

def invert(d):
    res = {}
    for v, k in d.iteritems():
        if k in res:
            res[k].append(v)
        else:
            res[k] = [v]
    return res


from mdict import *

def invert_dict(d):
    res = mdict()
    for v, k in d.iteritems():
        res[k] = v
    return res

print d
d2 = invert_dict(d)
print d2


from TurtleWorld import *

import math

world = TurtleWorld()
bob = Turtle(world)

def triangle(t):
    t.fd(60)
    t.lt(90)
    t.fd(80)
    t.lt(143.13)
    t.fd(100)

triangle(bob)
die(bob)
print math.atan(3.0/4) * 180 / math.pi

world.mainloop()
