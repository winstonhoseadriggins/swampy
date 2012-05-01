"""Solution to an exercise in Think Python by Allen Downey.

This module works with Swampy, a suite of programs available from
allendowney.com/swampy.

Copyright 2010 Allen B. Downey
Distributed under the GNU General Public License at gnu.org/licenses/gpl.html.
"""

from swampy.World import World

class Point:
    """Represents a 2-D point."""

def make_point(x, y, color):
    """Makes a point with the given coordinates and color."""
    p = Point()
    p.x, p.y = x, y
    p.color = color
    return p


class Rectangle:
    """Represents a rectangle."""

def make_rectangle(p, width, height):
    """Makes a rectangle with the given upper-left corner, width, height."""
    r = Rectangle()
    r.corner, r.width, r.height = p, width, height
    return r


def draw_point(canvas, point, size=2):
    """Draw a point as a circle on a canvas."""
    loc = [point.x, point.y]
    canvas.circle(loc, size, outline=None, fill=point.color)


def draw_rectangle(canvas, rect):
    """Draw a rectangle on a canvas."""
    point = rect.corner
    loc1 = [point.x, point.y]
    loc2 = [point.x+rect.width, point.y-rect.height]
    canvas.rectangle([loc1, loc2], outline=None, fill=point.color)


def main():
    width = 400
    height = 300

    world = World()
    canvas = world.ca(width=width, height=height, background='white')


    point = make_point(-width/2, height/2, 'red') 
    rect = make_rectangle(point, width, height)

    draw_point(canvas, point)
    draw_rectangle(canvas, rect)
    
    world.mainloop()


main()
