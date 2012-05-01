from swampy.World import *
from time import sleep

world = AmoebaWorld()
amy = Amoeba(world)

for i in range(10):
    amy.redraw(i, i)
    world.update()
    sleep(0.5)

world.mainloop()
