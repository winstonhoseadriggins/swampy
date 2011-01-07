import sys
from math import *

class Hypo(dict):
    """a hypothesis maps from each possible value of lamb to the
    likelihood of the value (or probability, if normalized).
    lamb is the parameter of the exponential distribution.
    """
    def update(self, x):
        """update this hypothesis with this datum, which is
        a measure of the distance from the source where a
        decay event was detected
        """
        for lamb in self:
            Z = exp(-1.0/lamb) - exp(-20.0/lamb)
            likelihood = exp(-x/lamb) / lamb / Z
            self[lamb] *= likelihood

    def normalizing_constant(self):
        """compute the normalizing constant for this hypothesis,
        which is the sum of the likelihoods of the micro-hypotheses.
        """
        return sum(self.itervalues())

    def normalize(self):
        """normalize this hypothesis so that the probabilities
        sum to 1.0
        """
        nc = self.normalizing_constant()
        for lamb in self:
            self[lamb] /= nc


def make_uniform(n=10):
    """make a hypothesis with n equally spaced micro-hypotheses
    between lamb=0+e and lamb=100, all with the same prior likelihood
    """
    h = Hypo()
    for i in range(n):
        lamb = 100.0 * (i+1) / n
        h[lamb] = 1.0
    h.normalize()
    return h


def main(name, *args):

    # make a uniform prior
    h = make_uniform(100)

    # the data from page 49
    data = [1.5, 2, 3, 4, 5, 12]

    # update the distribution and the normalize
    for x in data:
        h.update(x)
    h.normalize()

    # print the posterior distribution on logx scale
    t = h.items()
    t.sort()
    for lamb, like in t:
        print log10(lamb), like

if __name__ == '__main__':
    main(*sys.argv)
