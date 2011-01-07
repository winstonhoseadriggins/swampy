import os

def etime():
    """see how much user and system time this process has used
    so far and return the sum"""
    user, sys, chuser, chsys, real = os.times()
    return user+sys


class ListQueue(list):
    def append(self, item):
        self.append(item)

    def pop(self):
        return self.pop(0)

    def is_empty(self):
        return len(self) != 0


class DictQueue(dict):
    """based on an implementation from the Python Cookbook
    (not sure about the original author)"""

    def __init__(self):
        self.nextin = 0
        self.nextout = 0

    def append(self, item):
        self.nextin += 1
        self[self.nextin] = item

    def pop(self):
        self.nextout += 1
        return dict.pop(self, self.nextout)

    def is_empty(self):
        return len(self) != 0


class Queue(object):

    def __init__(self, n=2):
        self.t = [None] * n
        self.first = 0
        self.num = 0

    def is_empty(self):
        return self.num == 0

    def append(self, item):
        if self.num == len(self.t):
            self.resize()

        index = (self.first + self.num) % len(self.t)
        self.t[index] = item
        self.num += 1;

    def extend(self, seq):
        for item in seq:
            self.append(item)

    def resize(self):
        new = Queue(len(self.t * 2))
        while not self.is_empty():
            new.append(self.pop())

        self.t = new.t
        self.first = new.first
        self.num = new.num
        

    def pop(self):
        self.num -= 1
        index = self.first
        self.first = (self.first + 1) % len(self.t)
        return self.t[index]
    

def test_func(f, n):
    """test the function (f) with a list of lists of length (n)
    and return the elapsed time."""
    q = f()

    start = etime()

    for i in range(n):
        q.append(i)

    while not q.is_empty():
        x = q.pop()

    end = etime()
    elapsed = end - start
    return elapsed

def main(script, name='ListQueue'):

    factor = 10000

    # look up the string (name) and get the function object
    f = eval(name)

    # test (f) over a range of values for (n)
    for i in range(1, 10):
        n = factor * i
        print n, test_func(f, n)

if __name__ == '__main__':
    import sys
    main(*sys.argv)
