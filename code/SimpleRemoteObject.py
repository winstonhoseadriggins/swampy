"""This file demonstrates a simple use of RemoteObject to
implement an addition server."""

from RemoteObject import *

class SimpleRemoteObject(RemoteObject):
    """this remote object exports the add method"""
    def add(self, x, y):
        print x, y
        return x + y

def server(name):
    """this is the code to start a SimpleRemoteObject server"""

    # instantiate the object
    simple = SimpleRemoteObject(name)

    # wait for requests
    simple.requestLoop()

def client(name, x, y):
    """this is the code for a SimpleRemoteObject client"""

    # find the name server
    ns = NameServer()

    # instantiate a proxy for the remote object
    proxy = ns.get_proxy(name)

    # invoke a method on the proxy
    z = proxy.add(x, y)
    print z

def main(script, name='bob', x=None, y=None, *args):
    if x != None and y != None:
        # if the user provides arguments, run as a client
        x = int(x)
        y = int(y)
        client(name, x, y)
    else:
        # otherwise run as a server
        server(name)
        
if __name__ == '__main__':
    main(*sys.argv)
