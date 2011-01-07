import random
from pylab import *
from Dist import Dist

def roll_dice(dice, sides=6):
    """roll (dice) dice with (sides) sides and return the sum
    """
    t = [random.randint(1,sides) for x in range(dice)]
    return sum(t)

num_dice = 3
sample_size = 100

d = Dist()
for i in range(sample_size):
    s = roll_dice(num_dice)
    d.count(s)

d.print_pdf()
d.plot_pdf()
show()
