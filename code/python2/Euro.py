import sys

class Hashable:
    def __hash__(self): return id(self)
    def __cmp__(self, other): return id(self)-id(other)

class Hypo(Hashable, dict):
    """a hypothesis maps from possible values of p to the
    likelihood of the value (or probability, if normalized).
    p is the probability of getting heads ('a').
    """
    def update(self, datum):
        """update this hypothesis with this data;
        datum is either 'a' or 'b'
        """
        for p in self:
            if datum == 'a':
                likelihood = p
            else:
                likelihood = 1-p
            self[p] *= likelihood

    def normalize(self):
        """normalize this hypothesis so that the probabilities
        sum to 1.0
        """
        nc = self.normalizing_constant()
        for p in self:
            self[p] /= nc

    def normalizing_constant(self):
        """compute the normalizing constant for this hypothesis,
        which is the sum of the likelihoods of the micro-hypotheses.
        """
        return sum(self.itervalues())


def make_uniform(n=10):
    """make a hypothesis with n+1 equally spaced micro-hypotheses
    between p=0 and p=1, all with the same likelihood
    """
    h = Hypo()
    low = 0.0
    high = 1.0
    
    for i in range(n+1):
        p = low + (high-low) * i / n
#        if 0.45 < p < 0.55: continue
        h[p] = 1.0
    h.normalize()
    return h

def main(name, *args):
    # h0 is the hypothesis that the coin is unbiased
    h0 = Hypo()
    h0[0.5] = 1

    # h1 is the hypothesis that the coin is biased with unknown p
    h1 = make_uniform(1000)

    # d will keep track of the likelihood of the hypotheses
    d = {}

    # the data are 250 trials, 140 heads
    data = ['a'] * 140 + ['b'] * 110

    for h in h0, h1:
        # update each hypothesis with the data
        for datum in data:
            h.update(datum)

        # the likelihood of a hypothesis is just the sum of the
        # likelihoods of the micro-hypotheses, which is just the
        # normalizing constant
        d[h] = h.normalizing_constant()

    # rather than compute posterior probabilities, we compute the
    # likelihood ratio, which tells us to what degree these data
    # support one hypothesis over the other.
    print d[h1] / d[h0]

if __name__ == '__main__':
    main(*sys.argv)
