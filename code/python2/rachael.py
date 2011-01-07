from Graph import *

class Link(Edge):
   """Link is an edge connecting two bee colonies"""

   def __init__(self, v, w, length=1):
       """each edge has an attribute length that represents the likelihood
       of transferring infection from one colony to the another """
       Edge.__init__(self, [v, w])
       self.length = length

v = Vertex('v')
w = Vertex('w')
l = Edge(v, w)
l.length = 2
print l
