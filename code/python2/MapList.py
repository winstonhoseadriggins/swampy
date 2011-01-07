"""
Title
A dictionary with multiple values for each key.

Summary

Often I find myself wanting to
accumulate all the values for a given key in a list.  The MapList
class provides a simple implementation of this feature.

Discussion

MapList is a subclass of the built-in dictionary in which
each key maps to a list of values.  By overriding __setitem__, it
changes the behavior of both the get method and the [] operator.

If d is a normal dictionary, then d[key]=value replaces the old value
for the given key, if there is one.

If d is a MapList, then d[key]=value appends value onto the list
of values for this key, creating a new list if necessary.

MapList inherits the constructor from dict, so it is up to the user to
initialize all values to lists.


"""


class MapList(dict):

    def __setitem__(self, key, value):
        """add the given value to the list of values for this key"""
        self.setdefault(key, []).append(value)

 
if __name__ == '__main__':
    ml = MapList()
    key = 'key'
    ml[key] = 'val1' 
    ml[key] = 'val2'
    print ml[key]

    d = {key:'value'}
    ml = MapList(d)
    ml[key] = 'val2'

