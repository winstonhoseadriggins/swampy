from Tkinter import *
from threading import *
from Queue import *
from math import *
from time import sleep
from random import *

from swampy.World import *

def run_in_thread(function, *args):
    thread = Thread(target=function, args=args)
    thread.start()
    return thread
 
class World(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.size = 20
        self.cx = 0
        self.cy = self.size
        
        self.canvas = Canvas(self, bg='white', width=400, height=400)
        self.canvas.pack()
        
        self.button = Button(self, text="QUIT", command=self.quit)
        self.button.pack()

        self.spinners = []
        for i in range(400):
            spinner = self.make_spinner()
            self.spinners.append(spinner)
            
    def quit(self):
        for spinner in self.spinners:
            spinner.running = 0
        sleep(0.5)
        Tk.quit(self)

    def make_spinner(self):
        self.cx += self.size
        if self.cx > 390:
            self.cx = self.size
            self.cy += self.size
        self.circle(self.cx, self.cy, self.size/2)    
        return Spinner(self)

    def circle(self, x, y, r, **options):
        coords = [[x-r, y-r], [x+r, y+r]]
        tag = self.canvas.create_oval(coords, **options)
        return tag


class Spinner:
    def __init__(self, world):
        self.world = world
        self.cx = world.cx
        self.cy = world.cy
        self.r = world.size / 2
        run_in_thread(self.spin)

    def spin(self):
        theta = 0
        tag = None
        
        self.running = 1
        while self.running:
            self.cx += randint(-1, 1)
            self.cy += randint(-1, 1)
            x = self.cx + self.r * cos(theta)
            y = self.cy + self.r * sin(theta)
            if tag: self.world.canvas.delete(tag)
            tag = self.world.circle(x, y, self.r, fill='red')
            theta += 0.1
            sleep(uniform(0.01, 0.2))

    def polar(self, x, y, r, theta):
        rad = theta * pi/180
        s = sin(rad)
        c = cos(rad)
        return [ x + r * c, y + r * s ]         

    def draw_line(self, scale, dtheta, **options):
        r = scale * self.r
        theta = self.theta + dtheta
        head = self.polar(self.x, self.y, r, theta)
        tail = self.polar(self.x, self.y, -r, theta)
        self.world.create_line([tail, head], **options)

    def draw(self):
        self.tag = 'Spinner%d' % id(self)
        lw = self.r/2
        self.draw_line(2.5, 0, tags=self.tag, width=lw, arrow=LAST)
        self.draw_line(1.8, 40, tags=self.tag, width=lw)
        self.draw_line(1.8, -40, tags=self.tag, width=lw)
        self.world.create_circle(self.x, self.y, self.r, self.color,
                                 tags=self.tag)
        if self.delay > 0:
            self.update()

world = World()
world.mainloop()
