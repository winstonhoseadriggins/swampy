"""

This module uses color_list and Tkinter
to get the X11 colors and draw a color grid.

Moving the mouse over a color displays the name(s).

Allen B. Downey
2008

"""

from swampy.World import *
from color_list import read_colors

def make_grid(canvas, rgbs):
    """draw a grid of colors from rgbs on the given canvas
    """
    row = 0
    col = 0
    size = 30
    cols = width/size
    for rgb, names in rgbs:
        x = col * size - width/2 + 1
        y = row * size - height/2 + 1
        bbox = [[x,y], [x+size, y+size]]
        for name in names:
            try:
                item = canvas.rectangle(bbox, fill=name)
                create_binding(item, names)
                break
            except:
                continue

        col += 1
        if col > cols:
            col = 0
            row += 1

def create_binding(item, names):
    """bind each color chit to handle mouse enter/leave events"""
    item.bind('<Enter>', Callable(enter, names))
    item.bind('<Leave>', Callable(leave))

def enter(names, event):
    """callback invoked when the mouse enters a chit"""
    text = ', '.join(names)
    textitem.config(text=text)

def leave(event):
    """callback invoked when the mouse enters a chit"""
    textitem.config(text='')

if __name__ == '__main__':
    world = World()
    width = 691
    height = 691
    canvas = world.ca(width=width, height=height, background='white')

    topleft = [-width/2+10, width/2-10]
    font = ("Courier", 18)
    textitem = canvas.text(topleft, text='', font=font, anchor=NW)

    colors, rgbs = read_colors()
    make_grid(canvas, rgbs)
    wait_for_user()
