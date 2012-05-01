#!/usr/bin/python

from Tkinter import *
from swampy.Gui import *
import os

class Hello(Gui):

    def __init__(self):
        Gui.__init__(self)
        self.ca_width = 400
        self.ca_height = 400
        self.transforms = [ CanvasTransform(self.ca_width, self.ca_height) ]
        self.setup()


    # setup creates the GUI elements (called widgets)
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
        self.bu(LEFT, text='Quit', command=self.quit)
        self.endfr()

        # the right frame is left open so that we can add widgets later
        # self.endfr()

    def hello(self):
        self.create_text([0, 0], 'Hello')

if __name__ == '__main__':

    # create the GUI
    h = Hello()

    # wait for user events
    h.mainloop()
