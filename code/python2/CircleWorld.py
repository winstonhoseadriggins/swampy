from TurtleWorld import *
import random

class CircleWorld(TurtleWorld):
    def setup(self):
        TurtleWorld.setup(self)
        self.setup_run()
        
    def step(self):
        if not hasattr(self, 'iters'):
            self.iters = [animal.step() for animal in self.animals]
            
        for iter in self.iters:
            try:
                iter.next()
            except StopIteration:
                pass
        

class CircleTurtle(Turtle):
    def step(self):
        angle = random.uniform(0, 360)
        self.rt(angle)
        self.pu()
        yield None
        self.fd(100)
        self.lt()
        yield None
        self.pd()
        self.fd(10)
        yield None
        self.die()
    

world = CircleWorld()

ts = [CircleTurtle(world, delay=0.01) for i in range(100)]

world.mainloop()
    
