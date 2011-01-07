import sys
import pylab

import populations
from Dist import *


def main(script, *args):
    t = populations.process()
    h = Hist(t)
    d = Dist(h)

    #d.print_cdf()

    pylab.subplot(1,2,1)
    d.plot_cdf(pylab.semilogx)

    pylab.subplot(1,2,2)
    d.plot_ccdf(pylab.loglog)

    pylab.show()

if __name__ == '__main__':
    main(*sys.argv)
