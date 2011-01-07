import random
import sys

alpha = float(sys.argv[1])
beta = float(sys.argv[2])

n = 10001

t = [int(random.weibullvariate(alpha, beta)) for i in range(n)]
t.sort()
print 1.0 * sum(t) / n, t[n/2]

#for x in t:
#    print x
