"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

from random import randint

try:
    # see if Swampy is installed as a package
    from swampy.TurtleWorld import *
except ImportError:
    # otherwise see if the modules are on the PYTHONPATH
    from TurtleWorld import *


class Wobbler(Turtle):
    """Represents a Turtle with attributes for speed and clumsiness."""

    def __init__(self, world, speed=1, clumsiness=60, color='red'):
        Turtle.__init__(self, world)
        self.delay = 0
        self.speed = speed
        self.clumsiness = clumsiness
        self.color = color

        # move to the starting position
        self.pu() 
        self.rt(randint(0,360))
        self.bk(150)

    def step(self):
        """Performs one step.

        Invoked by TurtleWorld on every Wobbler, once per time step.
        """
        self.steer()
        self.wobble()
        self.move()

    def move(self):
        """Moves forward in proportion to self.speed."""
        self.fd(self.speed)

    def wobble(self):
        """Makes a random turn in proportion to self.clumsiness."""
        dir = randint(0,self.clumsiness) - randint(0,self.clumsiness)
        self.rt(dir)

    def steer(self):
        """Steers the Wobbler in the general direction it should go.

        Postcondition: the Wobbler's heading may be changed, but
        its position may not.

        This method should be overridden by child classes.
        """
        self.rt(10)


def make_world(constructor):

    # create TurtleWorld
    world = TurtleWorld()
    world.delay = .01
    world.setup_run()

    # make three Wobblers with different speed and clumsiness attributes
    colors = ['orange', 'green', 'purple' ]
    i = 1.0
    for color in colors:
        t = constructor(world, i, i*30, color)
        i += 0.5

    return world


if __name__ == '__main__':
    world = make_world(Wobbler)
    world.mainloop()
