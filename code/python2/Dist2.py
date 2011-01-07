from pylab import *
from Dist import Dist

filename = 'ucb.lifetimes'
d = Dist()
d.process_file(filename)

d.print_cdf()
d.plot_cdf()
show()

