class Iterator:
    def __init__(self):
        self.data = [1, 2, 3]

    def __iter__(self):
        for i in self.data:
            yield i

iterator = Iterator()
for i in iterator:
    print i

