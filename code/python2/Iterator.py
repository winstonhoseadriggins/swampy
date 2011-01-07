class Iterator:
    def __init__(self):
        self.data = [1, 2, 3]
        self.index = 0

    def __iter__(self):
        return self

    def next(self):
        if self.index == len(self.data):
            raise StopIteration
        
        res = self.data[self.index]
        self.index += 1
        return res

iterator = Iterator()
for i in iterator:
    print i

