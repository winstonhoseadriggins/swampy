
class Trie(dict):
    def __init__(self, word=None, index=0):
        """make a new Trie that contains the given word,
        starting at the given index"""
        if word is not None:
            self.add_word(word, index)
    
    def add_word(self, word, index=0):
        """add the given word to the Trie, starting at the given index"""
        try:
            c = word[index]
            self[c].add_word(word, index+1)
        except IndexError:
            self[''] = EndTrie()
            return
        except KeyError:
            self[c] = Trie(word, index+1)

    def add_word2(self, word, index=0):
        """add the given word to the Trie, starting at the given index"""
        t = self
        for c in word[index:]:
            t = t.setdefault(c, Trie())
        t[''] = EndTrie()

    def list_all(self):
        """return a list of all the strings in the Trie"""
        return [c+s for c, v in self.iteritems() for s in v.list_all()] 

    def list_all(self):
        """return a list of all the strings in the Trie"""
        t = []
        for c, v in self.iteritems():
            for s in v.list_all():
                t.append(c+s)
        return t


    def has_word(self, word):
        t = self
        try:
            for c in word:
                t = t[c]
            return isinstance(t[''], EndTrie)
        except KeyError:
            return False

    def __len__(self):
        if self == {}: return 1
        return sum([len(v) for v in self.itervalues()])


class EndTrie(Trie):
    def list_all(self):
        return ['']
    
t = Trie()
t.add_word('allen')
t.add_word('all')
t.add_word('alien')

print t
print t.list_all()

print t.has_word('allen') 
print t.has_word('all')
print t.has_word('aliens')

print len(t)
