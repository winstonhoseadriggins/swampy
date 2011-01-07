from Gui import *
from RemoteObject import *

import threading

class MyThread(threading.Thread):
    """this is a wrapper for threading.Thread that improves
    the syntax for creating and starting threads.  See Appendix A
    of The Little Book of Semaphores, http://greenteapress.com/semaphores/
    """
    def __init__(self, target, *args):
        threading.Thread.__init__(self, target=target, args=args)
        self.start()

class Remote(RemoteObject):
    def __init__(self, n, parent=None):
        RemoteObject.__init__(self)        
        self.connect(ns)
        self.parent = parent
        self.total = 0

        if n == 0: return
        for i in range(2):
            MyThread(Remote, n-1, self.name)

        print 'hello'
        MyThread(Popup)
        self.requestLoop()

    def pay(self):
        self.total += 1


class Popup(Gui):
    def __init__(self, message=''):
        Gui.__init__(self)
        self.la(TOP, text=message)
        self.en(TOP)
        self.bu(TOP, text='Onward', command=self.callback)
        self.bu(TOP, text='Close', command=self.destroy)
        self.mainloop()

    def callback(self):
        pass
        

Watcher()
ns = NameServer()
Remote(1)
