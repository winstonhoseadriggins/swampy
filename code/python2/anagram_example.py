#!/usr/bin/python

from collections import Counter


def is_anagram(word1, word2):
    t = list(word2)
    for c in word1:
        if c not in t:
            return False
        t.remove(c)

    return len(t) == 0


print is_anagram('tachymetric', 'mccarthyite')
print is_anagram('banana', 'peach')


def is_anagram(word1, word2):
    t1 = sorted(list(word1))
    t2 = sorted(list(word2))
    return t1 == t2


def is_anagram(word1, word2):
    return sorted(list(word1)) == sorted(list(word2))


print is_anagram('tachymetric', 'mccarthyite')
print is_anagram('banana', 'peach')


def is_anagram(word1, word2):
    return Counter(word1) == Counter(word2)


print is_anagram('tachymetric', 'mccarthyite')
print is_anagram('banana', 'peach')


class Multiset(Counter):
    """A multiset is a Counter with all positive counts."""

    def is_subset(self, other):
        for char, count in self.items():
            if other[char] < count:
                return False
        return True


def can_spell(word, tiles):
    return Multiset(word).is_subset(Multiset(tiles))


print is_anagram('tachymetric', 'mccarthyite')
print is_anagram('banana', 'peach')

print can_spell('apple', 'aapples')
print can_spell('apple', 'aaples')
