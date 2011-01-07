
"""

Code example from _Computational_Modeling_
http://greenteapress.com/compmod

Copyright 2008 Allen B. Downey.
Distributed under the GNU General Public License at gnu.org/licenses/gpl.html.

"""

from numpy import *
import pylab

def make_table():
    d = {}
    d[1,1,1] = 0
    d[1,1,0] = 0
    d[1,0,1] = 1
    d[1,0,0] = 1
    d[0,1,1] = 0
    d[0,1,0] = 0
    d[0,0,1] = 1
    d[0,0,0] = 0
    return d

class CA(object):
    """A CA is a cellular automaton; the parameters for __init__ are:
    rule:  an integer in the range 0-255 that represents the CA rule
           using Wolfram's encoding.
    n:     the number of rows (timesteps) in the result.
    ratio: the ratio of columns to rows.
    """

    def __init__(self, n=100):
        """n, m are the number of rows, columns.
        array is the numpy array that contains the data.
        next is the index of the next empty row.
        """
        self.table = make_table()
        self.n = n
        self.m = n*2 + 1
        self.array = zeros((n, self.m), dtype=int8)

        self.array[0, self.m/2] = 1
        self.next = 1

    def loop(self, steps=1):
        """execute the given number of time steps"""
        [self.step() for i in xrange(steps)]

    def step(self):
        """execute one time step by computing the next row of the array"""
        i = self.next
        self.next += 1

        for j in xrange(1,self.m-1):
            neighborhood = tuple(self.array[i-1, j-1:j+2])
            self.array[i,j] = self.table[neighborhood]

    def draw(self):
        """draw the CA using pylab.pcolor.  flipud puts the first
        row at the top; negating it makes the ones black."""
        pylab.gray()
        pylab.pcolor(-flipud(self.array))
        pylab.axis([0, self.m, 0, self.n])
        pylab.xticks([])
        pylab.yticks([])


def main(script, n=10):
    n = int(n)
    ca = CA(n)
    ca.loop(n-1)
    ca.draw()
    pylab.show()

if __name__ == '__main__':
    import sys
    main(*sys.argv)
