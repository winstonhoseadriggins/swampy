# Homework 4 Solutions
# Software Design
# Allen Downey

# Three things to notice:

# 1) The function process_file returns a dictionary
# that contains the words from the file and their
# frequencies.  I use this function twice, to analyze
# the book, and also to process the word list.

# 2) I used the function subtract to
# find the words that appear in the book but not in the
# dictionary.  This is a general-purpose function that
# is likely to be reusable.

# 3) The decorate-sort-undecorate (DSU) pattern I used to
# find the ten most common words.

# Here are the results from The Great Gatsby:

# There are 50444 words in the book.
# There are 5824 different words in the book.
# The ten most common words are:
# the     2405
# and     1573
# a       1409
# i       1392
# to      1153
# of      1119
# he      854
# in      806
# was     769
# The words in the book that aren't in the word list are:
#  7.15 monte disarray lapped magnanimous stunned settee [and many more...]

import sys
import string
import random

def process_line(line, h):
    """add the words in (line) to the histogram (h)"""
    global count

    # replace hyphens with spaces
    line = line.replace('-', ' ')

    # split the line using whitespace
    t = line.split()
    
    for word in t:
        # remove punctuation and convert to lowercase
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()

        # update the histogram
        h[word] = h.get(word, 0) + 1

def process_file(filename):
    """make and return a histogram that contains the words from
    the given file and the number of times they appear"""
    h = {}
    fp = open(filename, 'r')
    for line in fp:
        process_line(line, h)
    return h

def sorted_list(d):
    """make a list of the key-value pairs from d and
    sort them in descending order by value"""
    t = [(value, key) for (key, value) in d.items()]
    t.sort()
    t.reverse()
    return t

def subtract(d1, d2):
    """return a dictionary with all keys that appear in d1 but not d2"""
    res = {}
    for key in d1:
        if not d2.has_key(key):
            res[key] = 1
    return res

def total_words(h):
    """return the total of the frequencies in (h)"""
    return sum(h.values())

def random_word(h):
    """choose a random word from histogram (h) with probability in
    proportion to frequency"""
    index = random.randint(1, total_words(h))
    sum = 0
    
    for word, freq in h.items():
        sum += freq
        if sum >= index:
            return word

def main(name, filename, words='words.txt'):
    book = process_file(filename)
    print 'There are %d words in the book.' % total_words(book)
    print 'There are %d different words in the book.' % len(book)

    t = sorted_list(book)
    print 'The ten most common words are:'
    for (freq, word) in t[0:9]:
        print '%s\t%d' % (word, freq)

    words = process_file(words)
    diff = subtract(book, words)
    print "The words in the book that aren't in the word list are:"
    for word in diff:
        print word,

    print "\n\nHere are some random words from the book"
    for i in range(100):
        print random_word(book),
    
if __name__ == '__main__':
    main(*sys.argv)
