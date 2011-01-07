import sys
from math import *

class Hypo(dict):
    def update(self, k):
        """update the hypothesis with the observation that there
        were k passengers when the bus arrived.
        """
        for t in self:
            # compute the likelihood: there is no need to compute
            # the denominator, k!, because it doesn't depend on t.
            mu = 1
            mut = mu * t
            likelihood = exp(-mut) * pow(mut, k)
            self[t] *= likelihood

    def normalizing_constant(self):
        return sum(self.itervalues())

    def normalize(self):
        nc = self.normalizing_constant()
        for t in self:
            self[t] /= nc

def make_prior(n=10):
    h = Hypo()
    for i in range(n):
        t = 40.0 * (i+1) / n
        lamb = 0.1
        h[t] = lamb * exp(-lamb * t)
    h.normalize()
    return h

def main(name, *args):

    h = make_prior(1000)
    h.update(13)
    h.normalize()

    # print the posterior distribution
    t = h.items()
    t.sort()
    sum = 0
    for lam, like in t:
        sum += like
        print lam, sum

if __name__ == '__main__':
    main(*sys.argv)
