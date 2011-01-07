from TurtleWorld import *

class MyWorld(TurtleWorld):
    def setup(self):
        self.ca_width = 400
        self.ca_height = 400

        self.row([1,1])
        self.canvas = self.ca(width=self.ca_width, height=self.ca_height,
                              bg='white')

        self.col([0], sticky=N)

        self.row([1,1])
        self.bu(text='Print canvas', command=self.canvas.dump)
        self.bu(text='Quit', command=self.quit)
        self.endrow()

        self.bu(text='Draw circle', command=self.circle)

        # leave this column unclosed so we can add more stuff later
        # self.endcol()

    def circle(self):
        ca = self.canvas
        ca.circle([0, 0], 100, fill='red')

class MyTurtle(Turtle):
    def __init__(self, world, delay=0.5):
        Animal.__init__(self, world)
        self.r = 5
        self.heading = 0
        self.pen = IntVar()
        self.pen.set(1)
        self.color = StringVar()
        self.color.set('red')
        self.delay = delay
        self.draw()
        world.register(self)
    
    def fd(self, r=1, width=None):

        if width == None:
            width = int(self.world.en_w.get())
        
        x = self.x
        y = self.y
        p1 = [x, y]
        p2 = self.polar(x, y, r, self.heading)
        self.x = p2[0]
        self.y = p2[1]
        if self.pen.get():
            color = self.color.get()
            self.world.canvas.line([p1, p2], fill=color, width=width)
        self.redraw()

    def draw(self):
        self.tag = 'Turtle%d' % id(self)
        lw = self.r/2
        self.draw_line(2.5, 0, tags=self.tag, width=lw, arrow=LAST)
        self.draw_line(1.8, 40, tags=self.tag, width=lw)
        self.draw_line(1.8, -40, tags=self.tag, width=lw)
        self.world.canvas.circle([self.x, self.y], self.r, self.color.get(),
                                 tags=self.tag)

        # star-belly turtles have bellies with stars
        self.draw_star()
        self.update()
        

    def draw_star(self):
        x, y, r = self.x, self.y, self.r

        thetas = range(self.heading, self.heading+360, 360/10)
        rs = [0.9 * r, 0.4 * r] * 5

        coords = [self.polar(x, y, r, theta) for (r, theta) in zip(rs, thetas)]
        self.world.canvas.polygon(coords, fill='yellow', tags=self.tag)


    def dance(self):
        delay = self.delay
        self.delay = 0.001

        for i in range(4):
            self.snowflake(20, 120)
            self.rt()
            
        self.delay = delay
        
    def snowflake(self, len=300, angle=120):
        for i in range(3):
            self.koch(len)
            self.rt(angle)

    def koch(self, n):
        if n<3:
            self.fd(n)
            return
        for angle in [-60, 120, -60, 0]:
            self.koch(n/3.0)
            self.rt(angle)


class MyTurtleControl(TurtleControl):
    def setup(self):
        w = self.turtle.world

        w.col(bd=2, relief=GROOVE)
        w.la(text='Turtle Control')

        # ROW 1
        w.row([0,1,0,0])
        w.bu(text=' fd ', command=self.fd)
        self.en_r = w.en(width=5, text='10')
        w.bu(text='lt', command=self.turtle.lt)
        w.bu(text='rt', command=self.turtle.rt)
        w.endrow()

        # ROW 2
        w.row()
        w.cb(text='Pen', variable=self.turtle.pen)

        w.gr(2)
        colors = 'red', 'orange', 'yellow', 'green', 'blue', 'violet'
        for color in colors:
            w.rb(anchor=W, text=color, command=self.turtle.redraw,
                 variable=self.turtle.color, value=color)

        w.endgr()
        w.endrow()

        # ROW 3
        w.row()
        w.bu(text='dance', command=self.turtle.dance)
        w.endrow()
        
        # ROW 4
        w.gr(2)
        w.la(text='Line Width')
        b1 = w.bu(text='up')

        w.en_w = w.en(width=5, text='1')
        b2 = w.bu(text='down')

        b1.configure(command=Callable(incr_entry, w.en_w, 1))
        b2.configure(command=Callable(incr_entry, w.en_w, -1))

        w.endgr()
        w.endcol()


    def fd(self):
        r = int(self.en_r.get())
        self.turtle.fd(r)


def incr_entry(entry, val):
    old = int(entry.get())
    new = old + val
    entry.delete(0, END)
    entry.insert(END, str(new))

world = MyWorld()
bob = MyTurtle(world)
control = MyTurtleControl(bob)

world.mainloop()
