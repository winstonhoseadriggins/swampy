"""This program generates a UML diagram that demonstrates
class objects and class variables."""


import Lumpy
lumpy = Lumpy.Lumpy()

# normally class objects are opaque, meaning that Lumpy
# doesn't show their attributes, but you can change this
# behavior with the transparent_class method
clstype = type(Lumpy.Lumpy)
lumpy.transparent_class(clstype)

lumpy.make_reference()

# importing a module creates a module object
import random

class Cell:
    """a Cell is an element of a linked list (Chapter 17);
    car and cdr are historic names for the elements of a cell"""

    # cells is a class atttribute
    cells = []
    
    def __init__(self, car=None, cdr=None):
        self.car = car
        self.cdr = cdr
        Cell.cells.append(self)

    def __str__(self):
        return '<' + str(self.car) + ',' + str(self.cdr) + '>'

    def __hash__(self):
        return hash(self.car) ^ hash(self.cdr)

node1 = Cell('a')
node2 = Cell('b', node1)
node3 = Cell('c', node2)

cls = node1.__class__

lumpy.object_diagram()

