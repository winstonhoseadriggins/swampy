from RemoteObject import *
from time import sleep

class MyThread(threading.Thread):
    def __init__(self, target, *args):
        threading.Thread.__init__(self, target=target, args=args)
        self.start()

class MyRemoteObject(RemoteObject):
    def foo(self):
        print 'foo'
        bar('bob')

    def baz(self):
        print 'baz'

w = Watcher()
ns = NameServer()

def bar(name):
    print name
    ro = MyRemoteObject()
    ro.connect(ns, name)
    MyThread(ro.stoppableLoop)

bar('alice')
sleep(1)

p1 = ns.get_proxy('alice')
p1.foo()
sleep(1)

p2 = ns.get_proxy('bob')
p2.baz()
