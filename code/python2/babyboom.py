
"""

Code example from _Computational_Modeling_
http://greenteapress.com/compmod

Copyright 2008 Allen B. Downey.
Distributed under the GNU General Public License at gnu.org/licenses/gpl.html.

"""

fp = open('babyboom.dat')

for line in fp:
    if 'START DATA' in line:
        break

times = []
for line in fp:
    t = line.split()
    time = int(t[-1])
    times.append(time)


diffs = [times[0]]
for i in range(len(times)-1):
    diff = times[i+1] - times[i]
    diffs.append(diff)

print 1.0*sum(diffs)/len(diffs)

from Dist import *
h = Hist(diffs)
d = Dist(h)

pylab.subplot(1,2,1)
d.plot_cdf()
pylab.xlabel('interarrival time (minutes)')

pylab.subplot(1,2,2)
d.plot_ccdf(pylab.semilogy)
pylab.xlabel('interarrival time (minutes)')

pylab.show()
