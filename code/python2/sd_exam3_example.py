from TurtleWorld import *

class MyWorld(TurtleWorld):
    def setup(self):
        TurtleWorld.setup(self)
        self.bu(TOP, text='Draw circle', command=self.circle)

    def circle(self):
        ca = self.canvas
        ca.circle(0, 0, 100, fill='red')

class MyTurtle(Turtle):
    def draw(self):
        Turtle.draw(self)
        
        x, y, r = self.x, self.y, self.r
        options = dict(fill='yellow', tags=self.tag)
        self.world.canvas.circle(x, y, r/2.0, **options)


world = MyWorld()
bob = MyTurtle(world)

world.mainloop()
