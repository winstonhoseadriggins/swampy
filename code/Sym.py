import sys

class Variable:
    """a Variable represents a variable in a symbolic computation;
    the symbol attribute should be a one-character string"""
    def __init__(self, symbol):
        self.symbol = symbol

    def __str__(self):
        return self.symbol

    def __cmp__(self, other):
        return ord(self.symbol) - ord(other.symbol)


class Poly:
    """parent class for different implementations of polynomials"""

class DensePoly(Poly):
    """implementation of Poly using a list of coefficients, in order
    from low to high, so coefs=[1,2,3] represents 1 + 2x + 3x^2"""
    def __init__(self, var, coefs):
        self.var = var
        self.coefs = coefs
    
    def __str__(self):
        """return a string representation of this Poly"""
        t = []
        for i, coef in enumerate(self.coefs):
            s = '%d %s^%d' % (coef, str(self.var), i)
            t.append(s)
        res = ' + '.join(t)
        return res

    def convert_dense(self): 
        """return a dense representation of this Poly"""
        return self

    def convert_sparse(self):
        """return a sparse representation of this Poly"""
        d = dict(enumerate(self.coefs))
        return SparsePoly(self.var, d)

    def __add__(self, other):
        """add self and other and return a new Poly """
        if self.var != other.var:
            raise ValueError, 'Cannot add polynomials of different variables.'

        other = other.convert_dense()
        p = self.coef_sum(other.coefs)
        return p

    def coef_sum(self, coefs):
        """add the list of coefficients to this Poly and return a new Poly"""
        def sum(a,b):
            """return the sum of a and b, replacing any False value with 0"""
            return (a or 0) + (b or 0)
        t = map(sum, self.coefs, coefs)
        return DensePoly(self.var, t)

    def __mul__(self, other):
        """multiply self by other and return a new Poly"""
        # the body of this function is a placekeeper;
        # replace it with your correct implementation
        res = DensePoly(self.var, [0])
        return res

    # you can write helper methods and functions below
            
        
class SparsePoly(Poly):
    """implementation of Poly using a dictionary that
    maps from each power of var to a coefficient, 
    so coefs={0:1, 2:3} represents 1 + 3x^2"""
    def __init__(self, var, coefs):
        self.var = var
        self.coefs = coefs
    
    def __str__(self):
        """return a string representation of this Poly"""        
        t = []
        for i, coef in self.coefs.items():
            s = '%d %s^%d' % (coef, str(self.var), i)
            t.append(s)
        res = ' + '.join(t)
        return res

    def convert_dense(self): 
        """return a dense representation of this Poly"""
        # the body of this function is a placekeeper;
        # replace it with your correct implementation
        t = [0]
        return DensePoly(self.var, t)

    def convert_sparse(self):
        """return a sparse representation of this Poly"""
        return self

    def __add__(self, other):
        """add self and other and return a new Poly """
        if self.var != other.var:
            raise ValueError, 'Cannot add polynomials of different variables.'

        other = other.convert_sparse()
        return self.coef_sum(other.coefs)

    def coef_sum(self, coefs):
        """add the give coef dict to this Poly and return a new Poly"""
        d = self.coefs.copy()
        for i, coef in coefs.items():
            d[i] = d.get(i,0) + coef
        return SparsePoly(self.var, d)


def main(script, *args):
    x = Variable('x')
    p1 = DensePoly(x, [1,2,3])
    p2 = DensePoly(x, [4,5,6])

    p3 = p1 + p2
    print p3

    p4 = p1 * p2
    print p4

    # add your test code below this line


if __name__ == '__main__':
    main(*sys.argv)


