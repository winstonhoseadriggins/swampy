from random import normalvariate

n = 10000
count = 0

for i in range(n):
    x = normalvariate(176.2, 10.0)
    y = normalvariate(162.5, 9.0)
    if x > y:
        count += 1

print 1.0 * count / n
