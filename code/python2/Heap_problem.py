import heapq

class Heap(list):
    def __init__(self, t=[]):
        self.extend(t)
        self.heapify()

    heapify = heapq.heapify

n = 15
data = [i for i in range(10)]

heap = Heap(data)
