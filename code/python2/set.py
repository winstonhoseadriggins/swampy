import sys

def build_set(t):
    res = {}
    for item in t:
        res[item] = 1
    return res

def union(s1, s2):
    t = s1.copy()    # copy is a pure function
    t.update(s2)     # update is a modifier
    return t

def intersect(s1, s2):
    res = {}
    for key in s1:
        if key in s2:
            res[key] = 1
    return res

def main(*args):
    s1 = build_set(range(3))
    s2 = build_set([3, 2, 1])
    s3 = build_set('allen')

    print s1
    print s2
    print s3
    print intersect(s1, s2)
    print union(s1, s2)
    
if __name__ == '__main__':
    main(*sys.argv)
