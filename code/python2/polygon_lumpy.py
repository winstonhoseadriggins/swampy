# Homework 2 Solutions
# Software Design
# Allen Downey

from TurtleWorld import *

def polyline(t, n, length, angle):
    """draw n lines with the given length and
    the given angle between them"""
    lumpy.object_diagram()

    for i in range(n):
        fd(t, length)
        lt(t, angle)

def polygon(t, n, length):
    """draw an n-sided polygon with the given side length"""
    angle = 360.0/n
    polyline(t, n, length, angle)

import Lumpy
lumpy = Lumpy.Lumpy()
lumpy.opaque_class(TurtleWorld)
#lumpy.opaque_class(Turtle)

lumpy.make_reference()
world = TurtleWorld()
bob = Turtle(world)
polygon(bob, 10, 20)

import sys
sys.exit()


def arc(t, r, theta=360.0, length=1):
    """draw part of a circle with radius r and angle theta.
    using segments with the given length"""
    circum = 2 * pi * r * theta / 360.0
    n = int(ceil(circum / length))            # round up
    length = circum / n
    angle = 1.0 * theta / n
    polyline(t, n, length, angle)

def circle(t, r, length=1):
    """draw a circle with radius r, using segments with the given length"""
    arc(t, r, 360, length)

def petal(t, r, theta=30, length=1):
    """draw a petal by drawing two arcs with the given parameters"""
    for i in range(2):
        arc(t, r, theta, length)
        lt(t, 180-theta)

def flower(t, n=5, r=100, theta=60):
    """draw a flower with n petals, using arcs with the given parameters"""
    for i in range(n):
        petal(t, r, theta, 5)
        lt(t, 360.0/n)

def shape(t):
    """test circle and arc, and draw a cool shape"""
    length = 4
    for i in range(1,4):
        circle(t, i*30, length)
    for i in range(1,6):
        arc(t, i*30, 180.0, length)

if __name__ == '__main__':
    world = TurtleWorld()    

    bob = Turtle(world)
    bob.delay = 0.001
    shape(bob)

    ray = Turtle(world)
    ray.delay = 0.001
    flower(ray, 7, 150, 80)

    world.mainloop()
