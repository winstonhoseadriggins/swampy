#!/usr/bin/python

# Homework 5 Solutions
# Software Design
# Allen Downey

# This version of the random text generator demonstrates some
# object-oriented features.  A RandomText object has three attributes:
# a dictionary that maps prefixes onto a list of suffixes,
# a tuple named prefix that keeps track of the current prefix,
# and an integer named order that is the number of words in the
# prefix.

# An advantage of this solution is that we have encapsulated
# the state of a random text generator in an object, which eliminates
# the need for global variables, and makes it possible to perform
# more than one textual analysis at a time (to compare texts, for
# example).  Also, because order is an attribute of the object,
# we don't have to pass it around as a parameter.

import sys, string, random

class RandomText:
    def __init__(self, order=2):
        self.dict = {}     # the map from prefixes onto a list of suffixes
        self.prefix = ()   # the current prefix
        self.order = order # how many words in the prefix

    def process_file(self, filename):
        fp = open(filename, 'r')
        for line in fp:
            for word in line.rstrip().split():
                self.process_word(word)

    def process_word(self, word):
        # during the first two iterations, all we do is
        # store up the words
        if len(self.prefix) < self.order:
            self.prefix += (word,)
            return

        # add the new suffix to the end of the list
        self.dict.setdefault(self.prefix, []).append(word)

        # shift the prefix
        self.prefix = shift(self.prefix, word)

    # generate n random words
    def random_text(self, n=100):
        # choose a random prefix
        prefix = random.choice(self.dict.keys())
    
        for i in range(n):
            suffixes = self.dict.get(prefix, None)
            if suffixes == None:
                # if the prefix isn't in dict,
                # we got to the end of the original text, so
                # we have to start again to get the rest of the words
                self.random_text(n-i)
                return

            # choose a random suffix
            word = random.choice(suffixes)
            print word,
            prefix = shift(prefix, word)

def shift(t, word):
    """form a new tuple by removing the head and adding word to the tail.
    this is just a plain old function, not a method"""
    return t[1:] + (word,)
        
def main(name, filename='', n=100, order=2, *args):
    try:
        n = int(n)
        order = int(order)
        print n, order
    except:
        print 'The second and third arguments must be numbers'
    else: 
        rt = RandomText(order)
        rt.process_file(filename)
        rt.random_text(n)

if __name__ == '__main__':
    main(*sys.argv)
