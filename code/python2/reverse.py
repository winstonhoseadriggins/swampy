"""

Code example for Think Python
http://thinkpython.com

Copyright 2008 Allen B. Downey.
Distributed under the GNU General Public License at gnu.org/licenses/gpl.html.

"""

def in_both(word1, word2):
    for letter in word1:
        if letter in word2:
            print letter


def is_reverse(word1, word2):
    if len(word1) != len(word2):
        return False
    
    i = 0
    j = len(word2)-1

    while j > 0:
        print i, j
        
        if word1[i] != word2[j]:
            return False
        i = i+1
        j = j-1

    return True

def all_but_first(word):
    return word[1:]

def all_but_last(word):
    return word[:-1]

def is_reverse(word1, word2):
    print word1, word2
    if word1 == '' or word2 == '':
        return word1 == '' and word2 == ''

    if word1[0] != word2[-1]:
        return False

    return is_reverse(word1[1:], word2[:-1])

print is_reverse('pots', 'stop')
print is_reverse('spot', 'pots')
print is_reverse('ab', 'ba')
