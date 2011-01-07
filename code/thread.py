from threading import Thread
from time import sleep

def counter(xs, delay=1):
    for x in xs:
        print x
        sleep(delay)

# one thread counts backwards, fast
t = Thread(target=counter, args=[range(100, 1, -1), 0.25])
t.start()

# the other thread count forwards, slow
counter(range(1, 100), 1)

