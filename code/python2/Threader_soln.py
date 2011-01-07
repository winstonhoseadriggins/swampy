#!/usr/bin/python

from TurtleWorld import *

import os, threading, signal

class MyThread(threading.Thread):
    """this is a wrapper for threading.Thread that improves
    the syntax for creating and starting threads.
    """
    def __init__(self, target, *args):
        threading.Thread.__init__(self, target=target, args=args)
        self.start()

class Watcher:
    """this class solves two problems with multithreaded
    programs in Python, (1) a signal might be delivered
    to any thread (which is just a malfeature) and (2) if
    the thread that gets the signal is waiting, the signal
    is ignored (which is a bug).

    The watcher is a concurrent process (not thread) that
    waits for a signal and the process that contains the
    threads.  See Appendix A of The Little Book of Semaphores.
    http://greenteapress.com/semaphores/

    I have only tested this on Linux.  I would expect it to
    work on the Macintosh and not work on Windows.
    """
    
    def __init__(self):
        """ Creates a child thread, which returns.  The parent
            thread waits for a KeyboardInterrupt and then kills
            the child thread.
        """
        self.child = os.fork()
        if self.child == 0:
            return
        else:
            self.watch()

    def watch(self):
        try:
            os.wait()
        except KeyboardInterrupt:
            # I put the capital B in KeyBoardInterrupt so I can
            # tell when the Watcher gets the SIGINT
            print 'KeyBoardInterrupt'
            self.kill()
        sys.exit()

    def kill(self):
        try:
            os.kill(self.child, signal.SIGKILL)
        except OSError: pass


class Threader(Turtle):
    def __init__(self, world):
        Turtle.__init__(self, world, delay=0.005)
        self.set_color('purple')

    def step(self): pass

    def moveto(self, x, y):
        self.x = x
        self.y = y
        self.redraw()

    def koch(self, n):
        if n<8:
            self.fd(n)
            return
        for angle in [-60, 120, -60, 0]:
            self.koch(n/3.0)
            self.rt(angle)

    def snowflake(self):
        for i in range(3):
            self.koch(300)
            self.rt(120)
        self.undraw()
        

class ThreaderWorld(TurtleWorld):
    def __init__(self):
        self.watcher = Watcher()
        TurtleWorld.__init__(self)
    
    def quit(self):
        self.watcher.kill()

    def make_threader(self):
        t = Threader(self)
        t.moveto(-150, 90)
        MyThread(t.snowflake)

world = ThreaderWorld()
world.bu(LEFT, text='Make Threader', command=world.make_threader)
world.mainloop()

