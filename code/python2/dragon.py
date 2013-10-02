"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2013 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

from math import sqrt

try:
    # see if Swampy is installed as a package
    from swampy.TurtleWorld import *
except ImportError:
    # otherwise see if the modules are on the PYTHONPATH
    from TurtleWorld import *


ROOT2OVER2 = sqrt(2) / 2

def dragon(t, n, signum=1):
    """Draws a dragon curve with length n.

    Net effect is to move the Turtle forward by n.

    t: Turtle
    n: length
    signum: 1 or -1, indicates whether to draw a right or left-handed dragon
    """
    if n <= 4:
        fd(t, n)
    else:
        m = n * ROOT2OVER2
        rt(t, signum * 45)
        dragon(t, m, 1)
        lt(t, signum * 90)
        dragon(t, m, -1)
        rt(t, signum * 45)
    

world = TurtleWorld()
bob = Turtle()
bob.delay = 0

bob.x = -100
bob.redraw()

dragon(bob, 256, 1)

world.mainloop()
