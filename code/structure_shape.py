def structure_shape(ds):
    """return a string that describes the shape of the given
    data structure"""
    typename = type(ds).__name__

    sequence = (list, tuple)
    if isinstance(ds, sequence):
        s = set()
        for x in ds:
            s.add(get_shape(x))
        rep = '%s(%d) of %s' % (typename, len(ds), setrep(s))
        return rep

    elif isinstance(ds, dict):
        keys = set()
        vals = set()
        for k, v in ds.items():
            keys.add(get_shape(k))
            vals.add(get_shape(v))
        rep = '%s(%d) %s->%s' % (typename, len(ds), setrep(keys), setrep(vals))
        return rep

    else:
        return typename


def setrep(s):
    """return a string representation of a set of strings"""
    rep = ', '.join(s)
    if len(s) == 1:
        return rep
    else:
        return '(' + rep + ')'
    return 


if __name__ == '__main__':
    t = [1,2,3]
    print structure_shape(t)

    s = 'abc'
    print structure_shape(s)

    lt = zip(t, s)
    print structure_shape(lt)

    d = dict(lt)        
    print structure_shape(d)
