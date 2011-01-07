from TurtleWorld import *

class MyWorld(TurtleWorld):
    def setup(self):
        self.ca_width = 400
        self.ca_height = 400

        self.row()
        self.canvas = self.ca(width=self.ca_width, height=self.ca_height,
                              bg='white')

        self.col([1,1,1,1,1])
        
        self.row([1,1])
        self.bu(text='Print canvas', command=self.canvas.dump)
        self.bu(text='Quit', command=self.quit)
        self.endrow()

        # leave the column open so we can add more stuff later

class MyTurtle(Turtle):
    pass

class MyTurtleControl(TurtleControl):
    def setup(self):
        w = self.turtle.world

        self.frame = w.fr(bd=2, relief=SUNKEN)
        w.la(text='Turtle Control')

        # forward and back (and the entry that says how far)
        w.row([0,1,0])
        w.bu(text='bk', command=Callable(self.move_turtle, -1))
        self.en_dist = w.en(width=5, text='10')
        w.bu(text='fd', command=self.move_turtle)
        w.endrow()

        # other buttons
        w.row()
        w.bu(text='lt', command=self.turtle.lt)
        w.bu(text='rt', command=self.turtle.rt)
        w.bu(text='pu', command=self.turtle.pu)
        w.bu(text='pd', command=self.turtle.pd)

        colors = 'red', 'orange', 'yellow', 'green', 'blue', 'violet'

        # color menubutton
        w.row([0,1])
        w.la('Color:')
        self.mb = w.mb(text=colors[0])
        for color in colors:
            w.mi(self.mb, text=color, command=Callable(self.color, color))

world = MyWorld()
bob = MyTurtle(world)
control = MyTurtleControl(bob)

world.mainloop()
