"""Solution to an exercise from
Think Python: An Introduction to Software Design

Copyright 2010 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

This program requires Gui.py, which is part of
Swampy; you can download it from thinkpython.com/swampy.

"""

from swampy.Gui import *

g = Gui()
g.title('')
g.la('Select a color:')
colors = ['red', 'green', 'blue']
mb = g.mb(text=colors[0])

def set_color(color):
    print color
    mb.config(text=color)

for color in colors:
    g.mi(mb, text=color, command=Callable(set_color, color))

g.mainloop()
