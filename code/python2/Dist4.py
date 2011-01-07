import random
from Dist import Dist
from pylab import *

def roll_dice(dice, sides=6):
    """roll (dice) dice with (sides) sides and return the PRODUCT
    """
    t = [random.randint(1,sides) for x in range(dice)]

    prod = 1
    for x in t:
        prod *= x
    return prod

num_dice = 3
sample_size = 100

d = Dist()
for i in range(sample_size):
    s = roll_dice(num_dice)
    d.count(s)

subplot(1,2,1)
d.plot_cdf(semilogx)

subplot(1,2,2)
d.plot_ccdf(loglog)
show()
