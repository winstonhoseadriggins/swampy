#!/usr/bin/python

import string
import copy

class Hist(dict):
    def __init__(self, word):
        for c in word:
            self[c] = self.get(c, 0) + 1
        self.cat = self.category()
        print word, self.cat, self.items()

    def category(self):
        return [chr(self.get(c,0) + ord('a') -1) for c in 'aeiou']

    def is_subset(self, other):
        res = self.is_subset2(other)
        if other.cat < self.cat:
            if res == 1:
                print 'oddity'
                print self.cat, other.cat
                print self.items(), other.items()
        return res

    def is_subset2(self, other):
        for key, value in self.items():
            if value > other.get(key, 0):
                return 0
        return 1

    def is_empty(self):
        return self < Hist('')

    def subtract(self, other):
        res = copy.copy(self)
        for key in other.keys():
            res[key] = res.get(key, 0) - other[key];
            if res[key] == 0:
                del res[key]
        return res

    def sig(self):
        items = self.items()
        items.sort()
        return tuple(items)

    __lt__ = is_subset2
    __sub__ = subtract
    __invert__ = is_empty


class Dictionary(dict):
    def __init__(self, file='/usr/share/dict/words'):
        self.hint = {}
        fp = open(file, 'r')
        for word in fp:
            word = string.lower(string.strip(word))
            self[word] = Hist(word)

    def find_words(self, letters):
        words = []
        for key in self.keys():
            if self[key] < letters:
                words.append(key)
        return words

    def find_phrase(self, letters):
        sig = letters.sig()
        hint = self.hint.get(sig,None)
        if hint != None:
            return hint

        words = self.find_words(letters)
        print words
        res = []
        for word in words:
            remain = letters - Hist(word)
            if ~remain:
                res.append(word)
                
            phrases = self.find_phrase(remain)
            for phrase in phrases:
                res.append(word + ' ' + phrase)

        self.hint[sig] = res
        return res

if __name__ == '__main__':
    letters = Hist('allendowney')
    d = Dictionary()

    phrases = d.find_phrase(letters)
    for phrase in phrases:
        print phrase
