# Homework 5 Solutions
# Software Design
# Allen Downey

# This version of the random text generator doesn't use
# object-oriented features.

import sys
import string
import random

# global variables
map = {}               # the map from prefixes onto a list of suffixes
prefix = ()            # the current tuple of words

def process_file(filename, order=2):
    """read the given file and build the dictionary that maps
    each prefix to the list of possible suffixes.  The optional
    argument, order, controls the number of words in the prefixes."""
    for line in open(filename):
        for word in line.rstrip().split():
            process_word(word, order)

def process_word(word, order=2):
    """process each word.  During the first few iterations,
    all we do is store up the words; after that we start adding
    entries to the dictionary."""

    global prefix
    if len(prefix) < order:
        prefix += (word,)
        return

    try:
        map[prefix].append(word)
    except KeyError:
        # if there is no entry for this prefix, make one
        map[prefix] = [word]

    prefix = shift(prefix, word)

def random_text(n=100):
    """generate n random words, starting with a random prefix
    from the dictionary"""
    
    # choose a random prefix (not weighted by frequency)
    prefix = random.choice(map.keys())
    
    for i in range(n):
        suffixes = map.get(prefix, None)
        if suffixes == None:
            # if the prefix isn't in map, we got to the end of the
            # original text, so we have to start again.
            random_text(n-i)
            return

        # choose a random suffix
        word = random.choice(suffixes)
        print word,
        prefix = shift(prefix, word)

def shift(t, word):
    """form a new tuple by removing the head and adding word to the tail"""
    return t[1:] + (word,)

def main(name, filename='', n=100, order=2, *args):
    try:
        n = int(n)
        order = int(order)
    except:
        print 'Usage: randomtext.py filename [# of words] [prefix length]'
    else: 
        process_file(filename, order)
        random_text(n)

if __name__ == '__main__':
    main(*sys.argv)
