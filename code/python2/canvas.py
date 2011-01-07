#!/usr/bin/python

from Tkinter import *

class Ball:

    def __init__(self, world):
        self.x = 0
        self.y = 0
        self.radius = 10
        self.color = "red"
        world.register(self)

    def act(self):
        self.x = self.x + 1
        self.y = self.y + 1
        canvas = world.get_canvas()
        r = self.radius
        canvas.create_oval(self.x-r, self.y-r,
                                self.x+r,self.y+r)
        
class World:

    def __init__(self, master):
        self.master = master
        self.agents = []
        
        frame = Frame(master)
        frame.pack()

        left = Frame(frame)
        left.pack(side=LEFT)

        self.canvas = Canvas(left, bg="white", width=500, height=500)
        self.canvas.pack(side=TOP)

        right = Frame(frame)
        right.pack(side=LEFT)

        text = Text(right)
        text.pack(fill=Y)

        self.button = Button(right, text="Quit", command=frame.quit)
        self.button.pack()

        self.act()

    def register(self, agent):
        self.agents.append(agent)

    def act(self):
        self.canvas.delete(ALL)
        for a in self.agents:
            a.act()    
        self.master.after(10, self.act);

    def get_canvas(self):
        return self.canvas
    
    def draw(self, thing):
        print "hi there, everyone!"

root = Tk()

world = World(root)
ball = Ball(world)
ball.act()

root.mainloop()

