#!/usr/bin/python

from Tkinter import *

class World:

    def __init__(self):
        self.root = Tk()

        frame = Frame(self.root)
        frame.pack()

        self.button = Button(frame, text="QUIT", fg="red", command=frame.quit)
        self.button.pack(side=LEFT)

        self.hi_there = Button(frame, text="Hello", command=self.say_hi)
        self.hi_there.pack(side=LEFT)

        self.root.mainloop()

    def say_hi(self):
        print "hi there, everyone!"

world = World()

if isdefined(world.fred):
    print 'ok'
