import sys, random, threading
from time import sleep

class Semaphore(threading._Semaphore):
    wait = threading._Semaphore.acquire
    signal = threading._Semaphore.release

running = True
mutex = Semaphore(1)
num_cokes = 5

def consume():
    global num_cokes
    
    mutex.wait()
    num_cokes -= 1
    print num_cokes
    mutex.signal()

def produce():
    global num_cokes

    mutex.wait()
    num_cokes += 1
    print num_cokes
    mutex.signal()

def loop(f, mu=1):
# run function f over and over until running == False
# or there is a Keyboard interrupt
    global running

    print 'Running', str(f), 'in a loop.'
    
    try:
        while running:
            t = random.expovariate(mu)
            sleep(t)
            f()
    except KeyboardInterrupt:
        running = False

def thread_loop(*args):
# create a new thread to run loop, and start it
    thread = threading.Thread(target=loop, args=args)
    thread.start()
    return thread

def main(script, *args):
    global running

    # make a list of threads
    fs = [consume]*2 + [produce]*2 
    threads = [thread_loop(f) for f in fs]

    # the parent thread waits for a keyboard interrupt
    try:
        while running:
            sleep(1)
    except KeyboardInterrupt:
        running = False

    # and the joins with the child threads.
    for thread in threads:
        thread.join()

if __name__ == '__main__':
    main(*sys.argv)
