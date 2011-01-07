from math import *

class Location:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance(self, other):
        "compute the distance between Locations self and other"
        dx = self.x - other.x
        dy = self.y - other.y
        return sqrt(dx*dx + dy*dy)

    def isLeft(self, other): return self.x < other.x
    def isRight(self, other): return self.x > other.x
    def isAbove(self, other): return self.y > other.y
    def isBelow(self, other): return self.y < other.y

class Shape:
    "the parent class that all shapes inherit from"

class Circle(Shape):
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def contains(self, loc):
        """return True if Location loc is inside this circle
        (including the boundary)"""       
        return loc.distance(self.center) <= self.radius

class Rectangle(Shape):
    def __init__(self, topLeft, botRight):
        self.topLeft = topLeft
        self.botRight = botRight

    def contains(self, loc):
        """return True if Location loc is inside this rectangle
        (including the boundary)"""
        if loc.isLeft(self.topLeft): return False
        if loc.isRight(self.botRight): return False
        if loc.isAbove(self.topLeft): return False
        if loc.isBelow(self.botRight): return False
        return True

import Lumpy
lumpy = Lumpy.Lumpy()
lumpy.make_reference()

"make some Locations"
loc1 = Location(0, 10)
loc2 = Location(10, 0)

"make a list of shapes"
shape1 = Circle(loc1, 10)

shape2 = Rectangle(loc1, loc2)

lumpy.object_diagram()
lumpy.class_diagram()

