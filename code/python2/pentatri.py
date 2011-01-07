from TurtleWorld import *
from math import *

def ntri(t, n, r):
    theta = 360.0 / n
    for i in range(n):
        icosoles(t, r, theta/2)
        t.lt(theta)

def icosoles(t, r, theta):
    y = r * tan(theta*pi/180)
    x = sqrt(r**2 + y**2)

    t.rt(theta)
    t.fd(x)
    t.lt(90+theta)
    t.fd(2*y)
    t.lt(90+theta)
    t.fd(x)
    t.lt(180-theta)

world = TurtleWorld()
bob = Turtle(world)
bob.pu()
bob.bk(130)
bob.pd()

size = 40
for i in range(5, 9):
    ntri(bob, i, 40)
    bob.pu()
    bob.fd(size*2 + 10)
    bob.pd()
world.mainloop()
