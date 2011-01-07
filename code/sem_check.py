import sys
from threading import *

sem = Semaphore(1)
index = 0
size = 1000
array = [0] * size

def loop():
    global index

    while index < size:
        array[index] += 1
        index += 1

def run_in_thread(function, *args):
    thread = Thread(target=function, args=args)
    thread.start()
    return thread

def main(script, *args):

    t1 = run_in_thread(loop)
    t2 = run_in_thread(loop)

    t1.join()
    t2.join()

    print size
    for i in range(size):
        if array[i] != 1:
            print i, array[i]
        
if __name__ == '__main__':
    main(*sys.argv)
