#!/usr/bin/python

from math import pow
import operator

def norm(v):
    n = 0.5
    r = reduce(operator.add, [pow(x,n) for x in v])
    return pow (r, 1.0/n)

def geom(v):
    r = reduce(operator.mul, [x for x in v])
    return pow (r, 1.0/len(v))

def geom2(v, vp):
    v = [x-y for x, y in zip(v,vp)]
    r = reduce(operator.mul, [x for x in v])
    return pow (r, 1.0/len(v))

def tenure(list):
    vp = [0, 1, 2]
    score = geom2(list,vp) / geom2((6,6,6),vp)
    print str(list) + ' => ' + str(score)


tenure((6,6,6))
print ''
tenure((5,6,7))
tenure((7,6,5))
print ''
