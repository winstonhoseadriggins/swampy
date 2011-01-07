from Dist import *
from random import *
import pylab

def one_year(n=100, rate=0.001):
    t = [1 for i in range(n) if random()<=rate]
    return len(t)

def m_years(m=10, n=100, rate=0.001):
    t = [one_year(n, rate) for i in range(m)]
    return sum(t)

def find_dist(n=1, days=365, mu=950, sig=50):
    sample = [choose_loaf(n, mu, sig) for i in range(days)]
    print n, pylab.average(sample), pylab.std(sample)
    h = Hist(sample)
    d = Dist(h)
    return d


t = [m_years(m=10, n=100, rate=0.001) for i in range(1000)]
h = Hist(t)
d = Dist(h)
d.print_cdf()
d.plot_cdf()
d.show()
