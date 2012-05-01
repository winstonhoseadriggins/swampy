from swampy.World import *
from RemoteObject import *
from threading import *
import os

def run_in_thread(function, *args):
    thread = Thread(target=function, args=args)
    thread.start()
    return thread

class Popup(Gui):
    def __init__(self, message=''):
        Gui.__init__(self)
        self.la(TOP, text=message)
        self.bu(TOP, text='Close', command=self.destroy)
        run_in_thread(self.mainloop)
        
class IMServer(RemoteObject):
    def popup(self, message):
        Popup(message)

def main(script, name=None, *args):
    if name==None:
        name = os.getlogin()
    print 'Starting IMServer %s...' % name
    server = IMServer(name)
    server.requestLoop()
    
if __name__ == '__main__':
    main(*sys.argv)
