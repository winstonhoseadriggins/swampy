from swampy.TurtleWorld import *
import random

world = TurtleWorld()

ts = [Turtle(world, delay=0.01) for i in range(100)]

for t in ts:
    angle = random.uniform(0, 360)
    t.rt(angle)
    t.pu()
    t.fd(100)
    t.lt()
    t.pd()
    t.fd(10)
    t.die()
    
world.mainloop()
    
