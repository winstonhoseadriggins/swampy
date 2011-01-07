def merge(s, t):
    r = []
    try:
        while s or t:
            r.append(min(s,t).pop(0))
    except IndexError:
        r.extend(s+t)
    return r

def mergesort(t):
    mid = len(t)//2
    if mid == 0: return t
    return merge(mergesort(t[:mid]), mergesort(t[mid:]))


def msort(t):
    s = [[x] for x in t]
    while len(s) > 1:
        s.append(merge(s.pop(0), s.pop(0)))
    return s[0]
            

from random import *

t = [randrange(10) for i in range(20)]
print t
r = msort(t)
print r

t.sort()
print r == t
