import sys
import string
from math import *
from random import *

class Hypo(list):
    """a hypothesis is a list of lists, where each tuple is
    (tank, p), where tank is a hypothetical number of tanks
    and p is the likelihood of the value (or probability, if normalized).
    """
    def update(self, data):
        """update this hypothesis with this data;
        the data are the serial numbers of captured tanks
        """
        cap = len(data)
        m = max(data)
        f = 1
        
        for i, pair in enumerate(self):
            x, p = pair
            if x < m:
                pair[1] = 0
            else:
                pair[1] *= f
                f *= 1.0 * (x+1-cap) / (x+1)

    def normalize(self):
        """normalize this hypothesis so that the probabilities
        sum to 1.0
        """
        nc = self.normalizing_constant()
        for pair in self:
            pair[1] /= nc

    def normalizing_constant(self):
        """compute the normalizing constant for this hypothesis,
        which is the sum of the likelihoods of the micro-hypotheses.
        """
        t = [p for x, p in self]
        return 1.0 * sum(t)

    def interval(self, ps):
        i = 0
        xs = [None] * len(ps)
        sum = 0
        for x, p in self:
            sum += p
            if sum > ps[i]:
                xs[i] = x
                i += 1
                if i == len(ps):
                    return xs


def make_uniform(n=10, low=1, high=6000):
    """make a hypothesis with n+1 equally spaced micro-hypotheses
    between low and high, all with the same likelihood
    """
    t = [[x, 1] for x in xrange(low,high)]
    h = Hypo(t)
    h.normalize()
    return h


def estimate(data):
    m = max(data)
    
    h = make_uniform(1000, m, 4000)
    h.update(data)
    h.normalize()
    return h.interval([0.25, 0.75])
    

def main(name, *args):
    tanks = 3400
    cap = 100

    n = 1000
    count = 0
    for i in range(n):
        data = sample(xrange(tanks), cap)
        e = estimate(data)
        if e[0] < tanks < e[1]:
            count += 1
    print 1.0 * count / n
        

if __name__ == '__main__':
    main(*sys.argv)

