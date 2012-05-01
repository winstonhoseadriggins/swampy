#!/usr/bin/python

from __future__ import generators
from swampy.World import *
from random import *
import math
import sys

class Dancer(Turtle):
    def __init__(self, world):
        Turtle.__init__(self, world)
        self.delay = 0

    def step(self):
        print 'step'
        for i in range(19):
            self.lt()
#            yield None

# create a new TurtleWorld
world = TurtleWorld()
world.delay = .01

# add the Run, Stop, Step and Clear buttons
world.setup_run()

# add the Make Dancer button
world.fr()
world.bu(LEFT, text='Make Dancer', command=Callback(Dancer, world))
world.endfr()

Dancer(world)
world.mainloop()

