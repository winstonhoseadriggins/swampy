import time
import numpy

class Life(object):


    def __init__(self, n=100):
        """n, m are the number of rows, columns.
        array is the numpy array that contains the data.
        next is the index of the next empty row.
        """
        self.n = n
        self.array = numpy.zeros((n, n), dtype=numpy.int8)
        self.next = numpy.zeros((n, n), dtype=numpy.int8)

    def random(self):
        self.array = numpy.random.random([self.n,self.n]).round()
        a = self.array
        for i in xrange(self.n):
            a[0,i] = 0
            a[self.n-1,i] = 0
            a[i,0] = 0
            a[0,self.n-1] = 0


    def loop(self, steps=1):
        """execute the given number of time steps"""
        [self.step() for i in xrange(steps)]

    def update(self, i, j, sum):
        live = self.array[i,j]
        sum -= live
        self.next[i,j] = (sum==3) or (live and (sum==4))

    def step(self):
        a = self.array
        b = self.next
        f = self.update
        numsum = numpy.sum
        rows, cols = a.shape

        for i in xrange(1, rows-1):
            for j in xrange(1, cols-1):
                f(i, j, numsum(a[i-1:i+2, j-1:j+2]))

        # swap the arrays
        self.array, self.next = b, a

    def get_array(self, start=0, end=None):
        """get a slice of columns from the CA, with slice indices
        (start, end).  Avoid copying if possible.
        """
        if start==0 and end==None:
            return self.array
        else:
            return self.array[:, start:end]


import CADrawer                

class LifeDrawer(CADrawer.PILDrawer):

    def __init__(self):
        # we only need to import these modules if a PILDrawer
        # gets instantiated
        global Image, ImageDraw, ImageTk, Gui
        import Image
        import ImageDraw
        import ImageTk
        import Gui
        
    def draw(self, ca, start=0, end=None):
        a = ca.get_array(start, end)
        self.rows, self.cols = a.shape
        self.csize = 3
        size = [self.cols * self.csize, self.rows * self.csize]

        self.image = Image.new(mode='1', size=size, color=255)
        self.gui = Gui.Gui()
        command = Gui.Callable(self.step, ca)
        self.button = self.gui.bu(command=command, relief=Gui.FLAT)
        self.draw = ImageDraw.Draw(self.image)
        self.draw_array(numpy.flipud(a))

    def animate(self, ca, steps=10, delay=0.5):
        self.draw(ca)
        for i in xrange(10):
            self.step(ca)

    def step(self, ca, start=0, end=None):
        ca.step()
        a = ca.get_array(start, end)
        self.clear()
        self.draw_array(numpy.flipud(a))
        self.tkpi = ImageTk.PhotoImage(self.image)
        self.button.config(image=self.tkpi)
        self.gui.update()

    def cell(self, i, j):
        size = self.csize
        color = 0
        x, y = i*size, j*size
        self.draw.rectangle([x, y, x+size-1, y+size-1], fill=color)

    def rectangle(self, x, y, width, height, outline=0):
        self.draw.rectangle([x, y, x+width, y+height], outline=outline)

    def clear(self):
        self.draw.rectangle(((0,0), self.image.size), outline=255, fill=255)

    def show(self):
        self.tkpi = ImageTk.PhotoImage(self.image)
        self.button.config(image=self.tkpi)
        self.gui.mainloop()
 
    def save(self, filename='ca.gif'):
        self.image.save(filename)


def main(script, n=200, *args):
    n = int(n)
    ca = Life(n)
    ca.random()
    ca.step()

    #drawer = LifeDrawer()
    #drawer.animate(ca, 100)


if __name__ == '__main__':
    import sys
    #main(*sys.argv)

    import profile
    profile.run('main(*sys.argv)')
