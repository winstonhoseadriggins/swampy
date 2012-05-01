from swampy.Gui import *
from RemoteObject import *
#import threading

class MyThread(threading.Thread):
    def __init__(self, target, *args):
        threading.Thread.__init__(self, target=target, args=args)
        self.start()

class Remote(RemoteObject):
    def __init__(self, parent=None):
        RemoteObject.__init__(self)
        self.connect(ns)
        if parent == None:            
            self.pname = self.name
        else:
            self.pname = parent.name
        MyThread(Popup, self)

    def poke(self):
        self.gui.la(TOP, text='Ouch!')


class Popup(Gui):
    def __init__(self, remote):
        Gui.__init__(self)
        self.remote = remote
        remote.gui = self
        
        self.la(TOP, text=remote.name)
        self.fr(TOP)
        self.bu(LEFT, text='Spawn', command=Callable(Remote, self.remote))
        self.bu(LEFT, text='Poke', command=self.callback)
        self.bu(LEFT, text='Close', command=self.destroy)
        self.endfr()
        self.mainloop()

    def callback(self):
        ro = ns.get_proxy(self.remote.pname)
        ro.poke()
        
Watcher()
ns = NameServer()
ro = Remote().threadLoop()
