
from swampy.TurtleWorld import *

class CokeWorld(World):

    def __init__(self):
        World.__init__(self)
        self.ca_width = 400
        self.ca_height = 400
        self.animals = []
        self.thread = None

        self.row()
        self.canvas = self.ca(width=self.ca_width, height=self.ca_height,
                              bg='white', scale=[20,20])

        # draw the grid
        dash = {True:'', False:'.'}
        (xmin, xmax) = (-10, 10)
        (ymin, ymax) = (-10, 10)
        for x in range(xmin, xmax+1, 1):
            self.canvas.line([[x, ymin], [x, ymax]], dash=dash[x==0])
        for y in range(ymin, ymax+1, 1):
            self.canvas.line([[xmin, y], [xmax, y]], dash=dash[y==0])

    def control_panel(self):
        self.col()
        
        self.row()
        self.bu(text='Run', command=self.run_thread)
        self.bu(text='Stop', command=self.stop)
        self.bu(text='Quit', command=self.quit)
        self.endrow()

        self.endcol()


    def run_thread(self):
        # if there is already a thread, kill it and wait for it to die
        if self.thread:
            self.running = 0
            self.thread.join()

        # find out how long to run
        end = self.en_end.get()
        end = int(end)

        # create a thread and start it
        self.thread = Thread(target=self.run, args=[end])
        self.thread.start()

    def run(self, end=10):
        pass
            

class CokeTurtle(Turtle):

    def __init__(self, world, xoft=None, yoft=None):
        self.world = world
        self.xoft = xoft or self.xoft
        self.yoft = yoft or self.yoft
        self.color = 'red'
        world.register(self)


# create the GUI
world = CokeWorld()
world.control_panel()

# wait for the user to do something
world.mainloop()


