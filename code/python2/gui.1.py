#!/usr/bin/python

from Tkinter import *
import math
from random import *
import string
import os

debug = 0

class Gui:
    def __init__(self):
        self.root = Tk()
        self.frame = self.root     # the current frame
        self.frames = []           # the stack of nested frames

    def mainloop(self):
        self.root.mainloop()
        
    def quit(self):
        self.root.quit()

    # the following are wrappers on the tk widgets

    def fr(self, side=TOP, fill=NONE, expand=0, anchor=CENTER, **options):
        # save the current frame, then create the new one
        self.frames.append(self.frame)
        if debug:
            options['bd'] = 1
            options['relief'] = SOLID
        self.frame = self.widget(Frame, side, fill, expand, anchor, **options)
        return self.frame
    
    def endfr(self):
        self.frame = self.frames.pop()

    def tl(self, side=TOP, fill=NONE, expand=0, anchor=CENTER, **options):
        # save the current frame, then create the new one
        self.frames.append(self.frame)
        self.frame = Toplevel(options)
        return self.frame
    
    def ca(self, side=TOP, fill=NONE, expand=0, anchor=CENTER, **options):
        return self.widget(Canvas, side, fill, expand, anchor, **options)

    def la(self, side=TOP, fill=NONE, expand=0, anchor=CENTER, **options):
        return self.widget(Label, side, fill, expand, anchor, **options)

    def bu(self, side=TOP, fill=NONE, expand=0, anchor=CENTER, **options):
        return self.widget(Button, side, fill, expand, anchor, **options)

    def mb(self, side=TOP, fill=NONE, expand=0, anchor=CENTER, **options):
        mb = self.widget(Menubutton, side, fill, expand, anchor,
                         **options)
        mb.menu = Menu(mb, relief=SUNKEN)
        mb['menu'] = mb.menu
        return mb

    def mi(self, mb, label='', **options):
        mb.menu.add_command(label=label, **options)        

    def en(self, side=TOP, fill=NONE, expand=0, anchor=CENTER,
           text='', **options):
        en = self.widget(Entry, side, fill, expand, anchor, **options)
        en.insert(0, text)
        return en

    def te(self, side=TOP, fill=NONE, expand=0, anchor=CENTER, **options):
        return self.widget(Text, side, fill, expand, anchor, **options)

    def widget(self, constructor,
               side=TOP, fill=NONE, expand=0, anchor=CENTER, **options):
        widget = constructor(self.frame, options)
        widget.pack(side=side, fill=fill, expand=expand, anchor=anchor)
        return widget

    # the following are wrappers on the tk canvas items

    def trans(self, coords):
        for trans in self.transforms:
            coords = trans.trans_list(coords)
        return coords

    def create_circle(self, x, y, r, fill='', **options):
        options['fill'] = fill
        coords = self.trans([[x-r, y-r], [x+r, y+r]])
        tag = self.canvas.create_oval(coords, options)
        return tag;
    
    def create_oval(self, coords, fill='', **options):
        options['fill'] = fill
        return self.canvas.create_oval(self.trans(coords), options)

    def create_rectangle(self, coords, fill='', **options):
        options['fill'] = fill
        return self.canvas.create_rectangle(self.trans(coords), options)

    def create_line(self, coords, fill='black', **options):
        options['fill'] = fill
        tag = self.canvas.create_line(self.trans(coords), options)
        return tag;
    
    def create_polygon(self, coords, fill='', **options):
        options['fill'] = fill
        return self.canvas.create_polygon(self.trans(coords), options)

    def create_text(self, coord, text='', fill='black', **options):
        options['text'] = text
        options['fill'] = fill
        return self.canvas.create_text(self.trans([coord]), options)

    def itemconfig(self, tag, **options):
        self.canvas.itemconfig(tag, options)

    def itemcget(self, tag, option):
        return self.canvas.itemcget(tag, option)

    def delete_item(self, tag):
        self.canvas.delete(tag)

    def print_canvas(self):
        ps = self.canvas.postscript()
        fp = os.popen('lpr', 'w')
        fp.write(ps)
        fp.close()


class Hello(Gui):
    def __init__(self):
        Gui.__init__(self)
        self.ca_width = 400
        self.ca_height = 400
        self.transforms = [ CanvasTransform(self.ca_width, self.ca_height) ]
        self.setup()
        self.mainloop()

    def setup(self):
        # left frame
        self.fr(LEFT)
        self.canvas = self.ca(width=self.ca_width, height=self.ca_height,
                              bg='white')
        self.endfr()

        # right frame
        self.fr(LEFT, fill=BOTH, expand=1)

        self.fr()
        self.bu(LEFT, text='Hello', command=self.hello)
        self.bu(LEFT, text='quit', command=self.quit)
        self.endfr()

    def hello(self):
        self.create_text([0, 0], 'Hello')
              

class Callback:
    # see Python Cookbook 9.1, page 302
    
    def __init__(self, callback, *args, **kwds):
        self.callback = callback
        self.args = args
        self.kwds = kwds

    def __call__(self):
        return apply(self.callback, self.args, self.kwds)

class Transform:

    def trans_list(self, points):
        return [self.trans(p) for p in points]

    def invert_list(self, points):
        return [self.invert(p) for p in points]
    

class CanvasTransform(Transform):

    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def trans(self, p):
        x =  p[0] + self.width/2
        y = -p[1] + self.height/2      
        return [x, y]


if __name__ == '__main__':
    Hello()
