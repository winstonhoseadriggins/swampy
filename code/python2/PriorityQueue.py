import sys, Queue, bisect

class PriorityQueue(Queue.Queue):
    def _put(self, item):
        bisect.insort(self.queue, item)        


def main(script):
    # usage
    queue = PriorityQueue(0)
    queue.put((2, "second"))
    queue.put((1, "first"))
    queue.put((3, "third"))
    print queue

    priority, value = queue.get()
    print priority, value

    
if __name__ == '__main__':
    main(*sys.argv)
