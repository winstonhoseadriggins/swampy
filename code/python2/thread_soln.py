"""Example code using Python threads.

Copyright 2010 Allen B. Downey
imdb.py:License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

from threading import Thread
from time import sleep

from remote_object import MyThread, Watcher

def cleanup():
    print 'Cleaning up.'

Watcher(cleanup)

def counter(xs, delay=1):
    for x in xs:
        print x
        sleep(delay)

# one thread counts backwards, fast
MyThread(counter, range(100, 1, -1), 0.25)

# the other thread count forwards, slow
counter(range(1, 100), 1)

