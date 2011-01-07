class Bob(object):
    __slots__ = ('x','y')
    
b = Bob()
print b.__slots__.iteritem()
print b.__dict__

b.x = 0
