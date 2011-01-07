import random
from math import fabs

# n = number of respondents with one male child
n = 250
t = []

# run the simulation 1000 times
for j in range(1000):

    # p is the percentage of Rs with one child who want another
    p = 43.0 / 384

    # generate a random set of n Rs
    xs = [random.random() for i in range(n)]

    # count the number that want another child
    xs = [1 for x in xs if x <= p]
    total = len(xs)

    # compute the difference between the simulated and expected number
    t.append(total - p*n)

# compute the difference between the actual and expected number
diff = 30 - p * n

# how often did the simulation differ from expectations by
# as much as the actual number?
out = [1 for d in t if fabs(d) >= diff]
print len(out)
