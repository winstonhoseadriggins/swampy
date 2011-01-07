
# Note: this is an example of a BAD MERGESORT.
# The runtime is n^2 log n because pop(0) is linear.

def mergesort(t):
    """given a list (t), return a new list that contains 
    the elements of t in ascending order."""
    n = len(t)
    if n <= 4:
        ts = t[:]
        ts.sort()
        return ts

    t1 = mergesort(t[:n/2])
    t2 = mergesort(t[n/2:])
    ts = merge(t1, t2)
    return ts
    

def merge(t1, t2):
    """given two lists (t1, t2) that are sorted in ascending
    order, return a new list that contains the elements from
    both lists in ascending order."""
    ts = []
    while t1 and t2:
        t = min(t1, t2)
        ts.append(t.pop(0))
        
    ts.extend(t1)
    ts.extend(t2)
    return ts


from random import shuffle

t = range(10)
shuffle(t)

ts = mergesort(t)    
print ts
