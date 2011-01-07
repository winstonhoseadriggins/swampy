import string
import random
from Graph import *
from GraphWorld import *

def main(script, n='26', *args):

    # create n Vertices
    n = int(n)
    labels = string.lowercase + string.uppercase + string.punctuation
    vs = [Vertex(c) for c in labels[:n]]

    # create a graph and a layout
    g = Graph(vs)
    #g.add_regular_edges(25)
    g.add_all_edges()
    layout = CircleLayout(g)

    # draw the graph
    gw = GraphWorld()
    gw.show_graph(g, layout)
    gw.mainloop()


if __name__ == '__main__':
    main(*sys.argv)






