#!/usr/bin/python

class Tuple:

    def __init__(self, *comps):
        self.comps = comps

    def dim(self):
        return len(self.elts)

    def __add__(self, other):
        if self.dim() != other.dim(): raise ArithmeticError
        return [x+y for x,y in zip(self.elts, other.elts)]

    # dot product
    def __mul__(self, other):
        # check for scalars
        if self.dim() != other.dim(): raise ArithmeticError
        return reduce(lambda a,b: a+b,
                      [x*y for x,y in zip(self.elts, other.elts)])

    __rmul__ = __mul__
    
    # cross product
    def cross(self, other):
        if self.dim() != other.dim(): raise ArithmeticError
        return 1

    # automatic delegation as in Recipe 5.8, page 180
    def __getattr__(self, attr):
        return getattr(self.comps, attr)

    def __setattr__(self, attr, value):
        return setattr(self.comps, attr, value)


class Vector:

    def __init__(self, *pairs):
        assert len(pairs) > 0
        for t,c in pairs:
            assert isinstance(t, Tuple)
            assert isinstance(c, Coord)
        self.frames = pairs

    def project(self, coord):
        # check whether coord is in pairs
        # see if we have one that is just a shift
        # see if we have one that is just a rotation
        t,c = pairs[0]
        pair = (coord.project(t,c), coord)
        self.pairs.append(pair)


class Basis:

    def __init__(self, *units):
        for u in units:
            assert isinstance(u, Tuple)
        assert is_orthogonal(units)
        self.units = units


class Coord:
    
    def __init__(self, origin, basis):
        assert isinstance(origin, Tuple)
        assert isinstance(basis, Basis)
        self.origin = origin
        self.basis = basis

    def project(self, other, t):
        assert isinstance(other, Coord)
        assert isinstance(t, Tuple)
        v1 = self.origin - other.origin
        temp = t + shift
        for u in self.basis:
            comp = 0
            for v, c in zip(other.basis, t):
                comp += c * u * v
            result.append(comp)
        return result + v1

        
class CartCoord(Coord):
    pass


def is_orthogonal(units):
    return True




t = Tuple(1, 2, 3)
print isinstance(t, Tuple)
print t[1]
#t2 = Tuple(1, 2, 3)
#basis = Basis(Tuple(1,0,0), Tuple(0,1,0), Tuple(0,0,1))
#origin = Tuple(0,0,0)
#f = Coord(basis)
#print f
#print t+t2
#print t*t2
