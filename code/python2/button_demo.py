"""Solution to an exercise from
Think Python: An Introduction to Software Design

Copyright 2010 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

This program requires Gui.py, which is part of
Swampy; you can download it from thinkpython.com/swampy.

"""

from Gui import *

g = Gui()
g.title('')

def callback1():
    g.bu(text='Now press me.', command=callback2)

def callback2():
    g.la(text='Nice job.')

g.bu(text='Press me.', command=callback1)

g.mainloop()
