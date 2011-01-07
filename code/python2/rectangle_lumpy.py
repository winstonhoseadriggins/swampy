import Lumpy
lumpy = Lumpy.Lumpy()
lumpy.make_reference()

class Rectangle:
    pass

class Point:
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

