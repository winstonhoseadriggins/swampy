from random import *
from Dist import *

n = 9000
p = paretovariate
t1 = [100 * p(1.7) for i in xrange(n)]

p = normalvariate
t2 = [p(150, 50.0/3) for i in xrange(n)]

h1 = Hist(t1)
d1 = Dist(h1)

h2 = Hist(t2)
d2 = Dist(h2)

pylab.subplot(1,2,1)
pylab.hold(True)
d2.plot_cdf(pylab.semilogx, 'b-', label='Gaussian', linewidth=2)
d1.plot_cdf(pylab.semilogx, 'r--', label='Pareto', linewidth=3)
pylab.legend(loc='lower right')

pylab.subplot(1,2,2)
pylab.hold(True)
d1.plot_ccdf(pylab.loglog, 'r--', label='Pareto', linewidth=3)
d2.plot_ccdf(pylab.loglog, 'b-', label='Gaussian', linewidth=2)
pylab.legend(loc='upper right')



pylab.show()

