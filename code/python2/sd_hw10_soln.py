from TurtleWorld import *
from threading import *
import Queue

class Threader(Turtle):
    def __init__(self, world):
        Turtle.__init__(self, world)
        self.delay = 0.01
        self.set_color('purple')

    def step(self): pass
    # Threaders don't need no stinking step method.

    def moveto(self, x, y):
        self.x = x
        self.y = y
        self.redraw()

    def koch(self, n):
        if not self.running:
            sys.exit()
        if n<8:
            self.fd(n)
            return
        for angle in [-60, 120, -60, 0]:
            self.koch(n/3.0)
            self.rt(angle)

    def snowflake(self):
        self.running = 1
        for i in range(3):
            self.koch(300)
            self.rt(120)
        self.undraw()
        
def run_in_thread(function, *args, **kwargs):
    thread = Thread(target=function, args=args, kwargs=kwargs)
    thread.start()
    return thread

def make_threader(world):
    t = Threader(world)
    t.moveto(-150, 90)
    thread = run_in_thread(t.snowflake)

class ThreaderWorld(TurtleWorld):

    def quit(self):
        for animal in self.animals:
            animal.running = 0
        TurtleWorld.quit(self)

world = ThreaderWorld()
world.bu(LEFT, text='Make Threader', command=Callable(make_threader, world))
world.mainloop()

