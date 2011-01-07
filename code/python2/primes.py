    
def primegen():
    """Yields the sequence of prime numbers
    via the Sieve of Eratosthenes.

    David Eppstein, UC Irvine, 28 Feb 2002
    http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/117119
    """
    d = {}
    q = 2
    while True:
        p = d.pop(q, None) 
        if p:
            x = p + q
            while x in d: x += p
            d[x] = p
        else:
            d[q*q] = q
            yield q
        q += 1

primeiter = primegen()
primelist = [primeiter.next()]

def prime(n):
    while n >= len(primelist):
        more = [primeiter.next() for i in xrange(len(primelist))]
        primelist.extend(more)
    return primelist[n]

s = '~VIE=0s(),+*'
nums = range(1, len(s)+1)

lookup = dict(zip(s, nums))
revlook = dict(zip(nums, s))

def vargen():
    i = 5
    while 1:
        yield prime(i)
        i += 1

numiter = vargen()
sentiter = vargen()
prediter = vargen()

class Variable:
    def __init__(self, name, iter, exp):
        self.name = name
        self.num = iter.next()**exp

    def __str__(self):
        return self.name

def numvar(name): return Variable(name, numiter, 1)
def predvar(name): return Variable(name, prediter, 2)
def sentvar(name): return Variable(name, sentiter, 3)

def make_variables():
    for name in 'xyzn':
        var = numvar(name)
        lookup[name] = var.num
        revlook[var.num] = var.name

    for name in 'pqr':
        var = sentvar(name)
        lookup[name] = var.num
        revlook[var.num] = var.name

    for name in 'PQRAG':
        var = predvar(name)
        lookup[name] = var.num
        revlook[var.num] = var.name


def encode(s):
    prod = 1
    for i, c in enumerate(s):
        x = lookup[c]
        p = prime(i)
        print p, x
        prod *= p**x
    return prod

def decode(n):
    t = []
    i = 0
    while n>1:
        p = prime(i)

        j = 0
        while 1:
            q, r = divmod(n, p)
            if r:
                i += 1
                t.append(revlook[j])
                break
            j += 1
            n = q
    return ''.join(t)
            

            
if __name__ == '__main__':
    make_variables()

    g = encode('(Ex)(x=sy)')
    print g
    s = decode(g)
    print s
