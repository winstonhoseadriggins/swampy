# Solutions to exercises from "How to Think..."
# Allen B. Downey

from TurtleWorld import *
from math import *

def polypies(t, ns, r):
    """use turtle (t) to draw a row of polypies with some space between.
    (ns) is a list of integers specifying the number of sides in each pie.
    (r) is the spoke length of all pies.
    (t) ends at the starting position and orientation.
    """
    for i in ns:
        polypie(bob, i, 40)
        bob.pu()
        bob.fd(r*2 + 10)
        bob.pd()
    
def polypie(t, n, r):
    """use turtle (t) to draw a pie with (n) triangular slices with
    spoke length (r).  (n) must be greater than 2.
    (t) ends at the starting position, orientation.
    """
    theta = 360.0 / n
    for i in range(n):
        icosoles(t, r, theta/2)
        t.lt(theta)

def icosoles(t, r, theta):
    """use turtle (t) to draw an equilateral triangle with leg length
    (r) and peak angle (theta) in degrees.  (t) starts and ends
    at the peak, facing the middle of the base.
    """
    y = r * sin(theta*pi/180)

    t.rt(theta)
    t.fd(r)
    t.lt(90+theta)
    t.fd(2*y)
    t.lt(90+theta)
    t.fd(r)
    t.lt(180-theta)

# create the world and bob
world = TurtleWorld()
bob = Turtle(world)
bob.pu()
bob.bk(130)
bob.pd()

# draw polypies with various number of sides
ns = [5, 6, 7]
size = 40
polypies(bob, ns, size)
die(bob)

# dump the contents of the campus to the file canvas.eps
world.canvas.dump()

wait_for_user()

