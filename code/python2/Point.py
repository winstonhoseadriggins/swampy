#!/usr/bin/python

class Point:
  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y

  def __str__(self):
    return '(' + str(self.x) + ', ' + str(self.y) + ')'

  def __add__(self, other):
    return Point(self.x + other.x, self.y + other.y)

  def __sub__(self, other):
    return Point(self.x - other.x, self.y - other.y)

  def __mul__(self, other):
    return self.x * other.x + self.y * other.y

  def __rmul__(self, other):
    return Point(other * self.x, other * self.y)

  def reverse(self):
    self.x, self.y = self.y, self.x

  def frontAndBack(front):
    from copy import copy
    back = copy(front)
    back.reverse()
    print str(front) + str(back)

p = Point (1, 2)
print p
p.reverse()
print p

def print_attributes(obj):
    for attr, val in obj.__dict__.items():
        print attr, getattr(obj, attr)

print_attributes(p)
