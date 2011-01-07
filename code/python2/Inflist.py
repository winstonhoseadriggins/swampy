import sys

class Inflist:
    def __init__(self, value):
        self.value = value

    def __getitem__(self, index):
        return self.value

    def __len__(self):
        return sys.maxint

t = Inflist(17)
print t[0], t[123], t[123456789]
print len(t)
