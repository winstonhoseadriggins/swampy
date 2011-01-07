# simple version using only things in the book
def has_duplicates(t):
    d = {}
    for x in t:
        if d.has_key(x):
            return True
        d[x] = "the value doesn't matter"
    return False

# a version that uses the id function to deal with
# non-hashable keys and the in operator 
def has_duplicates2(t):
    d = {}
    for x in t:
        y = id(x)
        if y in d:
            return True
        d[y] = None
    return False

# a version that uses the set type
def has_duplicates3(t):
    d = set()
    for x in t:
        y = id(x)
        if y in d:
            return True
        d.add(y)
    return False

# test all three versions
for test in [has_duplicates, has_duplicates2, has_duplicates3]:

    t = range(10) + list(string.lowercase)
    print test(t)

    t.append('a')
    print test(t)
# simple version using only things in the book
def has_duplicates(t):
    d = {}
    for x in t:
        if d.has_key(x):
            return True
        d[x] = "the value doesn't matter"
    return False

# a version that uses the id function to deal with
# non-hashable keys and the in operator 
def has_duplicates2(t):
    d = {}
    for x in t:
        y = id(x)
        if y in d:
            return True
        d[y] = None
    return False

# a version that uses the set type
def has_duplicates3(t):
    d = set()
    for x in t:
        y = id(x)
        if y in d:
            return True
        d.add(y)
    return False

# test all three versions
for test in [has_duplicates, has_duplicates2, has_duplicates3]:

    t = range(10) + list(string.lowercase)
    print test(t)

    t.append('a')
    print test(t)
