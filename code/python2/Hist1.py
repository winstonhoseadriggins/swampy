import sys
import string
from math import *

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

    def pdf(self):
        """return a list of tuples where each tuple is a value x
        and a frequency f.
        """
        # sort the x,f pairs in the dictionary by x
        t = self.items()
        t.sort()
        return t
        
    def cdf(self):
        """return a list of tuples where each tuple is a value x
        and the cumulative fraction of values less than or equal
        to x.  This is the empirical CDF of the values in the Hist.

        Note: the cdf makes more sense if the data values in the Hist
        are numeric, but this function works for any data type that
        can be sorted.
        """
        # FILL THIS IN
        return None
    
    def print_ccdf(self):
        """print the data for a ccdf (complementary cumulative
        distribution function) of the frequencies.  WARNING: this
        function might make your head hurt because the frequencies
        from the Zipf object are the data values in hist.
        """
        # print the complementary cdf on a log-log scale
        for x, p in self.cdf():
            if p==1.0: break
            print log10(x), log10(1-p)

    def print_pdf(self):
        """print the data for a pdf of the frequencies
        """
        # print the (unnormalized) pdf on a log-log scale
        for x, f in self.pdf():
            print log10(x), log10(f)

    def process_file(self, filename):
        fp = open(filename, 'r')
        for line in fp:
            x = float(line)
            self.count(x)

def main(name, filename='', flag=None, *args):
    z = Hist()
    z.process_file(filename)
    z.print_pdf()

if __name__ == '__main__':
    main(*sys.argv)
