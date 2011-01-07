#!/usr/bin/env python
# encoding: utf-8

"""Zeichne mit den Schildkröten ein Herz.

Dafür gehen erst beide SChildkröten getrennte Wege, nach links oben und rechts oben, um dann mit einem Halbkreis wieder zusammenzukommen. 
"""

# We need all functions and classes from TurtleWorld
from TurtleWorld import *

# Also we need the number pi
import math

# First, create the canvas for drawing by calling TurtleWorld
TurtleWorld()

# Get the first object: 
#: The turtle which will draw our lines. 
bab = Turtle()

#: Another turtle. 
nica = Turtle()

turtles = [bab, nica]

for i in turtles: 
    i.delay = 0.1

size = 50

for i in range(len(turtles)): 
      lt(turtles[i], 135 - 90*i)
for i in turtles: 
    for j in range(size): 
      fd(i, 2.35)

radius = size

circumference = 2 * math.pi * radius
#: Each step of radius is one side, so we have minimal diffrence from a circle. 
sides = radius
#: The circumference divided by the number of sides gives the length of one side. Here 1 step. Added to make the number of sides customizeable without having to rewrite the length, too. 
length = circumference / sides

angle = 360.0/sides

for i in range(int(sides / 1.6)): 
        # move length steps forward
        fd(turtles[0], length)
        # turn angle degrees to the left
        lt(turtles[0], 360 - angle)

for i in range(int(sides / 1.6)): 
        # move length steps forward
        fd(turtles[1], length)
        # turn angle degrees to the left
        lt(turtles[1], angle)


# Close the window only after the user clicks the close button on the window bars. 
wait_for_user()


