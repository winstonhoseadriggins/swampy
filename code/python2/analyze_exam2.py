import string

class AdjacencyTable:
    "map from each word in a text to the list of words that follow it"
    
    def __init__(self):
        self.prev = None            # the previous word 
        self.table = {}             # mapping from word to list of words

    def next_word(self, word):
        "process the next word in the text"
        if self.prev != None:
            self.add_pair(self.prev, word)
        self.prev = word

    def add_pair(self, prev, next):
        "add an entry to the table showing that (prev) is followed by (next)"
        if prev in self.table:
            self.table[prev].append(next)
        else:
            self.table[prev] = [ next ]


def process_file(filename):
    adj = AdjacencyTable()
    fp = open(filename, 'r')
    for line in fp:
        for word in line.split():
            word = word.strip(string.punctuation)
            adj.next_word(word)
    return adj

def invert_adj(adj):
    inv = AdjacencyTable()
    for prev in adj.table:
        for next in adj.table[prev]:
            inv.add_pair(next, prev)
    return inv


class Hist(dict):
    """a histogram is a dictionary that maps from each item (x) to the
    number of times the item has appeared (frequency, f)
    """

    def __init__(self, seq=[]):
        "create a new histogram starting with the items in seq"
        for x in seq:
            self.count(x)

    def count(self, x):
        "increment the counter associated with item x"
        self[x] = self.get(x, 0) + 1


def top_word_pairs(adj):
    h = Hist()
    for prev in adj.table:
        for next in adj.table[prev]:
            h.count((prev, next))

    t = []
    for k, v in h.iteritems():
        t.append((v, k))

    t.sort(reverse=True)
    return t[0:10]
        

adj = process_file('gatsby.txt')
t = top_word_pairs(adj)
for k, v in t:
    print k, v

#adj2 = invert_adj(adj)
#for k,v in adj2.table.iteritems():
#    print k, v
