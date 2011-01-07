#!/usr/bin/python

from TurtleWorld import *

# create a Lumpy object and capture reference state
import Lumpy
lumpy = Lumpy.Lumpy()
lumpy.opaque_class(Turtle)
lumpy.opaque_class(TurtleWorld)
lumpy.make_reference()

def half_o(t, n):
    fd(t, n)
    lt(t)
    fd(t, 2*n)           # while it is executing this line
    lumpy.object_diagram()
    lt(t)

def draw_o(t, n):
    half_o(t, n)
    half_o(t, n)

world = TurtleWorld()
bob = Turtle(world)
draw_o(bob, 30)
