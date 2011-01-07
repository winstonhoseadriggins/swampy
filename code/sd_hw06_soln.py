# Homework 6 Solutions
# Software Design
# Allen Downey

import math, sys
from random import randint
from TurtleWorld import *

class Missed(Exception):
    """this is the exception raised when a turtle tries to tag
    someone too far away"""

class Tagger(Turtle):
    def __init__(self, world, speed=1, clumsiness=60, color='red'):
        Turtle.__init__(self, world)
        self.delay = 0
        self.speed = speed
        self.clumsiness = clumsiness
        self.color = color
        self.it = 0
        self.sulking = 0
        self.goal = None

        # move to the starting position
        self.pu()
        self.rt(randint(0,360))
        self.fd(150)
        self.turn_toward()
        self.pd()

    def distance(self, x=0, y=0):
        """compute the distance from this turtle to the given point"""
        dx = self.x - x
        dy = self.y - y
        return math.sqrt(dx**2 + dy**2)

    def distance_from(self, other):
        """compute the distance between turtles"""
        return self.distance(other.x, other.y)

    def youre_it(self):
        """make this turtle 'it' """
        self.it = 1
        self.old_color = self.color
        self.color = 'blue'
        self.sulking = 200
        self.redraw()

    def not_it(self):
        """make this turtle not 'it' """
        self.it = 0
        self.color = self.old_color
        self.redraw()

    def away(self, x=0, y=0):
        """compute the angle (in degrees) that faces away from
        the given point"""
        dx = self.x - x
        dy = self.y - y
        heading = math.atan2(dy, dx)
        return heading * 180 / math.pi

    def flee(self, other):
        """set the goal to face away from the other turtle"""
        self.goal = self.away(other.x, other.y)
        
    def chase(self, other):
        """set the goal to face the other turtle"""
        self.goal = self.away(other.x, other.y) + 180

    def turn_toward(self, x=0, y=0):
        """turn to face the given point"""
        self.heading = self.away(x, y) + 180
        self.redraw()

    def closest(self, others):
        """return the animal in the list that is closest to self
        (not including self!)"""
        t = [(self.distance_from(animal), animal)
              for animal in others if animal is not self]
        (distance, animal) = min(t)
        return animal

    def apply_tag(self, other):
        """try to tag the other turtle.  if it is too far away,
        let the other turtle flee and raise an exception"""
        if self.distance_from(other) < 10:
            self.not_it()
            other.youre_it()
        else:
            other.flee(self)
            raise Missed

    def step(self):
        """step is invoked whenever the turtle is supposed to move"""

        # if we're sulking, skip a turn
        if self.sulking > 0:
            self.sulking -= 1
            if self.sulking == 0:
                self.color = 'red'
            return

        # if we're it, find try to tag the closest animal.
        # if the tag misses, chase!
        if self.it:
            target = self.closest(world.animals)
            try:
                self.apply_tag(target)
            except Missed:
                self.chase(target)

        # have to stay in bounds!!!
        if self.distance() > 200:
            self.turn_toward()

        # if we have a goal, we get two chances to turn toward it;
        # otherwise, make a random turn
        if self.goal:
            dirs = [self.randangle() for i in range(2)]
            dir = self.best_choice(dirs)
            self.goal = None
        else:
            dir = self.randangle()

        # make the turn, but keep heading in bounds
        self.lt(dir)
        self.heading = self.heading % 360
        
        # move forward according to the speed attribute
        self.fd(self.speed)

    def randangle(self):
        """choose a random angle according to the clumsiness attribute"""
        return randint(0,self.clumsiness) - randint(0,self.clumsiness)


    def best_choice(self, t):
        """find the turn in the list that would bring the turtle
        closest to the goal"""
        diff = [(diff_dir(self.heading+dt, self.goal), dt)
                 for dt in t]
        return min(diff)[1]

def diff_dir(angle1, angle2):
    """compute the difference between two angles expressed in degrees"""
    t1, t2 = min(angle1, angle2), max(angle1, angle2)
    return min(t2-t1, t1+360-t2)

# create a new TurtleWorld
world = TurtleWorld()
world.delay = .01
world.setup_run()

# make three Taggers with different speed and clumsiness attributes
color = [None, 'orange', 'green', 'purple' ]
for i in range(1,4):
    Tagger(world, i, i*30, color[i])

# the middle turtle is "it"
world.animals[1].youre_it()

# play!
world.mainloop()

