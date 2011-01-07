def extreme_dist(n=10, tanks=3400, captured=100):
    ms = [max(sample(xrange(tanks), captured)) for i in range(n)]
    ms.sort()
    return ms

def eval_pdf(ms, x):
    t = [(x, y) for y, x in enumerate(ms)]
    infinity = 1e3000
    i = bisect(t, (x, infinity))
    if i<2: return 0
    if i==len(t):
        i -= 1
    x1, y1 = t[i-2]
    x2, y2 = t[i-1]
    x3, y3 = t[i]
    print x1, x2, x3
    print y1, y2, y3
    d = 2.0 / (x3 - x1)
    print d
    
def pdf(xs):
    ps = [0.0] * len(xs)
    for i in range(1, len(xs)-1):
        h = 1
        while True:
            if i+h >= len(xs):
                break
            if xs[i+h] > xs[i-h]:
                ps[i] = 2.0 * h / (xs[i+h] - xs[i-h])
                break
            h += 1
        
    for x, p in zip(xs, ps):
        print x, p
    
def pdf(xs):
    ps = {}
    for i in range(1, len(xs)-1):
        d = xs[i+1] - xs[i-1]
        if d:
            print d
            ps[xs[i]] = 2.0 / d

    t = ps.keys()
    t.sort()
    for x in t:
        print x, ps[x]
    
def likelihood(n=1000, tanks=3400, cap=100):
    r = 1.0 * (tanks+1-cap) / (tanks+1)
    ls = [1.0] * n 
    for i in range(1,n):
        ls[i] = ls[i-1] * r
        print i, ls[i]
