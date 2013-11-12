"""This file contains code for use with "Think Bayes",
by Allen B. Downey, available from greenteapress.com

Copyright 2013 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from swampy.Lumpy import Lumpy

lumpy = Lumpy()
lumpy.make_reference()

class Rectangle(object):
    pass

class Point(object):
    pass

def find_center(box):
    corner = box.corner
    p = Point()
    p.x = box.corner.x + box.width/2
    p.y = box.corner.y + box.height/2
    
    lumpy.object_diagram()
    return p

box = Rectangle()
box.width = 100
box.height = 200
box.corner = Point()
box.corner.x = 10
box.corner.y = 20

center = find_center(box)

lumpy.class_diagram()
