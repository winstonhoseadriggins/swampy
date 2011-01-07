def multiset(ks, vs):
    d = {}
    for k, v in zip(ks, vs):
        d.setdefault(k, []).append(v)
    return d

keys = ['a', 'b', 'a']
vals = [1, 2, 3]
ms = multiset(keys, vals)
print ms
