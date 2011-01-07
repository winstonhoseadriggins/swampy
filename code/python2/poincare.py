from Dist import *
from random import *
import pylab

def choose_loaf(n=1, mu=950, sig=50):
    t = [gauss(mu, sig) for i in range(n)]
    return max(t)

def find_dist(n=1, days=365, mu=950, sig=50):
    sample = [choose_loaf(n, mu, sig) for i in range(days)]
    print n, pylab.average(sample), pylab.std(sample)
    h = Hist(sample)
    d = Dist(h)
    return d


d = find_dist(n=1, days=365, mu=1000, sig=35)
d.plot_cdf()
pylab.hold(True)

d = find_dist(n=100, days=365, mu=950, sig=50)
d.plot_cdf()

d.show()
