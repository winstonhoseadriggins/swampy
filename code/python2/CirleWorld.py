from World import *
import random

class CircleWorld(TurtleWorld):
    def step(self):
        if iters == None:
            iters = [animal.step() for animal in self.animals]
            
        for iter in iters:
            try:
                iter.next()
            except StopIteration:
                pass
        

class CircleTurtle(Turtle):
    def step(self):
        for t in ts:
            angle = random.uniform(0, 360)
            t.rt(angle)
            t.pu()
            yield
            t.fd(100)
            t.lt()
            yield
            t.pd()
            t.fd(10)
            yield
            t.die()
    

world = CircleWorld()

ts = [CircleTurtle(world, delay=0.01) for i in range(100)]

world.mainloop()
    
