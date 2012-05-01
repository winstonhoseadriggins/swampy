from swampy.World import *
from RemoteObject import *
from threading import *
import os

class Popup(Gui):
    """create a top-level window with a label and a Close button."""
    def __init__(self, message=''):
        Gui.__init__(self)
        self.la(text=message)
        self.bu(text='Close', command=self.destroy)
        self.mainloop()
        
class PopupServer(RemoteObject):
    """a PopupServer is a remote object that provides a method,
    popup() that takes a message and displays it in a Popup"""
    def popup(self, message):
        MyThread(Popup, message)

def main(script, name=None, *args):
    """name is the name of the remote object"""
    if name==None:
        name = 'RemotePopupObject'
    print 'Starting PopupServer %s...' % name
    server = PopupServer(name)
    server.requestLoop()
    
if __name__ == '__main__':
    main(*sys.argv)

