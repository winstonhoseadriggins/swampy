#!/usr/bin/python

from swampy.TurtleWorld import *

import Lumpy
lumpy = Lumpy.Lumpy()
lumpy.opaque_class(Interpreter)
lumpy.transparent_class(Gui)
lumpy.make_reference()

world = TurtleWorld()
bob = Turtle(world)

lumpy.object_diagram()
lumpy.class_diagram([Tk, Gui, World, TurtleWorld, Animal, Turtle])

