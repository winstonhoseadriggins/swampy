import math
import random
import sys

def minch(alpha, beta):
    y = random.random()
    x = beta * math.pow((1-y)/y, -1.0/alpha)
    return x


alpha = float(sys.argv[1])
beta = float(sys.argv[2])

n = 10001

t = [minch(alpha, beta) for i in range(n)]

for x in t:
    print x
