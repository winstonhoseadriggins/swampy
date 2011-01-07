
"""

Code example from _Computational_Modeling_
http://greenteapress.com/compmod

Copyright 2008 Allen B. Downey.
Distributed under the GNU General Public License at gnu.org/licenses/gpl.html.

"""

from TurtleWorld import *
import random

# make the color list
# (DebianRed is on the list, but for some reason it causes an error)
from color_list import read_colors
colors, rgbs = read_colors()
colors = colors.keys()
colors.remove('DebianRed')

class Highway(TurtleWorld):
    """a Highway is a TurtleWorld with a one-dimensional lane
    that spirals down the canvas.  Each Turtle has a position
    attribute, which gets projected onto the canvas by Highway.project.
    (rows) is the number of rows that spiral down the canvas."""
    def __init__(self):
        TurtleWorld.__init__(self)
        self.rows = 10.0
        self.delay = 0.01

    def length(self):
        """return the total length of this highway"""
        return self.ca_width * self.rows

    def project(self, turtle):
        """project (turtle) onto the highway by mapping its
        position onto the canvas and setting its x and y attributes"""
        p = 1.0 * turtle.position % self.length()
        turtle.x = p % self.ca_width
        turtle.y = p / self.ca_width * self.ca_height / self.rows

    def align(self, turtle):
        """align the turtle so it faces along the lane"""
        x = self.ca_width
        y = 1.0 * self.ca_height / self.rows
        angle = math.atan2(y, x)
        turtle.heading = angle * 180 / math.pi


class Driver(Turtle):
    """a Driver is a Turtle with a random position, speed and color"""
    def __init__(self, *args, **kwds):
        Turtle.__init__(self, *args, **kwds)
        self.delay = 0
        self.position = random.randrange(0, self.world.length())
        self.speed = random.randrange(4,8)
        self.color = random.choice(colors)

        self.world.align(self)
        self.world.project(self)
        self.redraw()

    def step(self):
        """during a time step each Driver checks the distance of the 
        Driver in front, chooses a speed accordingly, and moves forward."""

        # find the following distance
        dist = self.next.position - self.position
        if dist < 0:
            dist += self.world.length()

        # choose a speed and move (but don't overtake)
        self.choose_speed(dist)
        move = min(self.speed, dist)
        self.position += move

        # redraw
        self.world.project(self)
        self.redraw()

    def choose_speed(self, dist):
        """adjust the speed of the Driver according to the following
        distance."""
        pass
    

def make_drivers(n=50, driver=Driver):
    """make (n) drivers at random positions; return a list of Drivers.
    The second parameter (driver) is the constructor used to create
    the drivers."""
    t = []
    for i in range(n):
        turtle = driver(delay=0.0)
        t.append((turtle.position, turtle))

    # link up the drivers so each has an attribute (next) that
    # refers to the driver in front
    t.sort()
    turtles = [t[1] for t in t]
    for i in range(n-1):
        turtles[i].next = turtles[i+1]
    turtles[-1].next = turtles[0]

    return turtles


def make_highway(n=50, driver=Driver):
    """Make the highway and (n) drivers, then run the simulation.
    The second parameter (driver) is the constructor used to create
    the drivers."""

    # create the highway
    world = Highway()
    world.canvas.clear_transforms()
    world.setup_run()
    
    # create (n) drivers
    make_drivers(n, driver)

    # start the simulation, then wait for user events
    world.run()
    world.mainloop()


def main(script, n=50):
    n = int(n)
    make_highway(n)

if __name__ == '__main__':
    import sys
    main(*sys.argv)
