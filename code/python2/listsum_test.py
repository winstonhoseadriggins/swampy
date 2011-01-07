import random

lens=[5,5,5,5,5,5,5,5]

v=[]

for i in lens:

    l=[]

    for j in range(i):

        l.append(17)

    v.append(l)

print v
 

print sum(v, [])

