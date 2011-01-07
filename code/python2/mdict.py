"""
Title
A dictionary with multiple values for each key.

Summary

I often find myself wanting to accumulate all the values for a given
key in a list.  The mdict class provides a simple implementation of
this feature.

Discussion

mdict is a subclass of the built-in dictionary in which
each key maps to a list of values.  By overriding __setitem__, it
changes the behavior of both the get method and the [] operator.

If d is a normal dictionary, then d[key]=value replaces the old value
for the given key, if there is one.

If d is an mdict, then d[key]=value appends the new value onto the
list of values for this key, creating a new list if necessary.

mdict inherits the constructor from dict.  If the user initializes the
mdict by passing arguments to the constructor, the value for each
key-value pair must be list, or else subsequent __setitem__
invocations will fail.  Alternatively, we could have overriden the
constructor to check the types of the initial values and convert them
appropriately, but it is not clear that there is a general solution.


"""


class mdict(dict):

    def __setitem__(self, key, value):
        """add the given value to the list of values for this key"""
        self.setdefault(key, []).append(value)

 
if __name__ == '__main__':
    ml = mdict()
    key = 'key'
    ml[key] = 'val1' 
    ml[key] = 'val2'
    print ml[key]

    

