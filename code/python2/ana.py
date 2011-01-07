#!/usr/bin/python

class Hist(dict):
    def __init__(self, s):
        for c in s:
            self[c] = self.get(c, 0) + 1

def is_anagram2(s1, s2):
    return Hist(s1) == Hist(s2)

def is_anagram(s1, s2):
    l = list(s2)
    for c in s1:
	try:
	    l.remove(c)
        except ValueError:
            return 0
    return len(l) == 0

print is_anagram('tachymetric', 'mccarthyite')
print is_anagram('banana', 'peach')
