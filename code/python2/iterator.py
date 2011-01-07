
class AllTrue(object):
    def next(self):
        return True

    def __iter__(self):
        return self

print zip('abc', AllTrue())

