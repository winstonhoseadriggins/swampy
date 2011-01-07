from numpy import *
import pylab

def binary(n, digits):
    """return a tuple of (digits) integers representing the
    integer (n) in binary.  For example, binary(2,3) returns (0, 1, 0)"""
    t = []
    for i in range(digits):
        n, r = divmod(n, 2)
        t.append(r)

    return tuple(reversed(t))

def make_table(rule):
    """Return a table for the given CA rule.  The table is a 
    dictionary that maps 3-tuples to binary values.
    """
    table = {}
    for i, bit in enumerate(binary(rule, 8)):
        t = binary(7-i,3)
        table[t] = bit
    return table

def print_table(table):
    """print the table in LaTeX format"""
    t = table.items()
    t.sort(reverse=True)

    print '\\beforefig'
    print '\\centerline{'
    print '\\begin{tabular}{|c|c|c|c|c|c|c|c|c|}'
    print '\\hline'

    res = ['prev']
    for k, v in t:
        s = ''.join([str(x) for x in k])
        res.append(s)
    print ' & '.join(res) + ' \\\\ \n\\hline'

    res = ['next']
    for k, v in t:
        res.append(str(v))
    print ' &   '.join(res) + ' \\\\ \n\\hline'

    print '\\end{tabular}}'


class CA(object):
    """A CA is a cellular automaton; the parameters for __init__ are:
    rule:  an integer in the range 0-255 that represents the CA rule
           using Wolfram's encoding.
    n:     the number of rows (timesteps) in the result.
    ratio: the ratio of columns to rows.
    """

    def __init__(self, rule, n=100, ratio=2):
        """n, m are the number of rows, columns.
        array is the numpy array that contains the data.
        next is the index of the next empty row.
        """
        self.table = make_table(rule)
        self.n = n
        self.m = ratio*n + 1
        self.array = zeros((n, self.m), dtype=int8)

    def start_single(self):
        """start with one cell in the middle of the top row"""
        self.array[0, self.m/2] = 1
        self.next = 1

    def start_random(self):
        """start with random values in the top row"""
        self.array[0] = random.random([1,self.m]).round()
        self.next = 1

    def loop(self, steps=1):
        """execute the given number of time steps"""
        [self.step() for i in xrange(steps)]

    def step(self):
        """execute one time step by computing the next row of the array"""
        i = self.next
        self.next += 1

        a = self.array
        t = self.table
        for j in xrange(1,self.m-1):
            a[i,j] = t[tuple(a[i-1, j-1:j+2])]

    def get_array(self, start=0, end=None):
        """get a slice of columns from the CA, with slice indices
        (start, end).  Avoid copying if possible.
        """
        if start==0 and end==None:
            return self.array
        else:
            return self.array[:, start:end]



class Drawer(object):
    """Drawer is an abstract class that should not be instantiated.
    It defines the interface for a CA drawer; subclasses of Drawer
    should implement:

    draw(ca) : draw the given CA
    show()   : display a representation of the CA, if possible
    save(filename) : save a representation of the CA in (filename)
    """

    def draw_array(self, a):
        """iterate through array (a) and draw any non-zero cells"""
        for i in xrange(self.rows):
            for j in xrange(self.cols):
                if a[i,j]:
                    self.cell(j, self.rows-i-1)


class PyLabDrawer(Drawer):

    def draw(self, ca, start=0, end=None):
        """draw the CA using pylab.pcolor."""

        pylab.gray()
        a = ca.get_array(start, end)
        rows, cols = a.shape

        # flipud puts the first row at the top; 
        # negating it makes the non-zero cells black."""
        pylab.pcolor(-flipud(a))
        pylab.axis([0, cols, 0, rows])

        # empty lists draw no ticks
        pylab.xticks([])
        pylab.yticks([])

    def show(self):
        """display the pseudocolor representation of the CA"""
        pylab.show()

    def save(self, filename='ca.png'):
        """save the pseudocolor representation of the CA in (filename)."""
        pylab.savefig(filename)
    


import Image
import ImageDraw
import ImageTk
import Gui

class PILDrawer(Drawer):
    def draw(self, ca, start=0, end=None):
        a = ca.get_array(start, end)
        self.rows, self.cols = a.shape
        self.csize = 4
        size = [self.cols * self.csize, self.rows * self.csize]

        self.image = Image.new(mode='1', size=size, color=255)
        self.gui = Gui.Gui()
        self.button = self.gui.bu(command=self.gui.quit, relief=Gui.FLAT)
        self.draw = ImageDraw.Draw(self.image)
        self.draw_array(flipud(a))

    def cell(self, i, j):
        size = self.csize
        color = 0
        x, y = i*size, j*size
        self.draw.rectangle([x, y, x+size, y+size], fill=color)

    def rectangle(self, x, y, width, height, outline=0):
        self.draw.rectangle([x, y, x+width, y+height], outline=outline)

    def show(self):
        self.tkpi = ImageTk.PhotoImage(self.image)
        self.button.config(image=self.tkpi)
        self.gui.mainloop()
 
    def save(self, filename='ca.gif'):
        self.image.save(filename)


class EPSDrawer(Drawer):
    def __init__(self):
        self.cells = []

    def draw(self, ca, start=0, end=None):
        a = ca.get_array(start, end)
        self.rows, self.cols = a.shape
        self.draw_array(a)

    def cell(self, i, j):
        self.cells.append((i,j))
        
    def print_cells(self, fp):
        for i, j in self.cells:
            fp.write('%s %s c\n' % (i, j))

    def print_head(self, fp):
        fp.write('%!PS-Adobe-3.0 EPSF-3.0\n')
        fp.write('%%%%BoundingBox: -2 -2 %s %s\n' % (self.cols+2, self.rows+2))

        size = .9
        fp.write('/c {\n')
        fp.write('   newpath moveto\n')
        fp.write('   0 %g rlineto\n' % size)
        fp.write('   %g 0 rlineto\n' % size)
        fp.write('   0 -%g rlineto\n' % size)
        fp.write('   closepath fill\n')
        fp.write('} def\n')

    def print_outline(self, fp):
        fp.write('newpath 0.1 setlinewidth 0 0 moveto\n')
        fp.write('0 %s rlineto\n' % self.rows)
        fp.write('%s 0 rlineto\n' % self.cols)
        fp.write('0 -%s rlineto\n' % self.rows)
        fp.write('closepath stroke\n')

    def print_tail(self, fp):
        fp.write('%%EOF\n')

    def show(self):
        pass

    def save(self, filename='ca.eps'):
        fp = open(filename, 'w')
        self.print_head(fp)
        self.print_outline(fp)
        self.print_cells(fp)
        self.print_tail(fp)

    


def main(script, rule=30, n=100, *args):
    rule = int(rule)
    n = int(n)

    ca = CA(rule, n)

    if 'random' in args:
        ca.start_random()
    else:
        ca.start_single()

    ca.loop(n-1)

    if 'eps' in args:
        drawer = EPSDrawer()
    elif 'pil' in args:
        drawer = PILDrawer()
    else:
        drawer = PyLabDrawer()

    if 'trim' in args:
        drawer.draw(ca, start=n/2, end=3*n/2+1)
    else:
        drawer.draw(ca)

    drawer.show()
    drawer.save()


if __name__ == '__main__':
    import sys
    main(*sys.argv)
