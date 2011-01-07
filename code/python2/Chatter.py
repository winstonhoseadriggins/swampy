import os
from World import *
from RemoteObject import *
from random import randrange

class Chatter(Gui, RemoteObject):
    """a client that creates a GUI, connects to a Room, and
    allows the user to send text to other users in the same Room.
    """
    def __init__(self):
        Gui.__init__(self)
        RemoteObject.__init__(self)

        # get the user's name and generate a unique remote object name
        self.login = os.getlogin()
        self.name = 'chatter_%s%d' % (self.login, randrange(1000))

        # register with the name server
        self.ns = NameServer()
        try:
            self.connect(self.ns, self.name)
            print self.name
        except Pyro.errors.NamingError:
            print "Couldn't register the name " + self.name
            sys.exit()

    def setup(self):
        """create the GUI"""
        self.col()
        self.display = self.st()          # scrollable text box

        self.row()
        self.entry = self.en()
        self.entry.insert(0, 'hello')
        self.bu(text='Send', command=self.send)
        self.bu(text='Quit', command=self.quit)

        self.entry.bind('<Return>', self.send)
        self.endrow()

        self.endcol()

    def join_room(self, room_name):
        """add this chatter to the given room"""
        try:
            print 'Looking for %s...' % room_name
            self.room = self.ns.get_proxy(room_name)
            print 'Joining room %s...' % room_name
            self.room.join(self.name)
        except:
            print "Couldn't join %s." % room_name
            print sys.exc_info()
            self.cleanup()
            sys.exit()
        
    def quit(self):
        """shut down and clean up"""
        try:
            self.room.unjoin(self.name)
        except: pass
        self.stopLoop()
        Gui.quit(self)

    def send(self, event=None):
        """send a message to the Room"""
        message = self.entry.get()
        self.room.send_message(self.login + ": " + message)

    def display_message(self, message):
        """display a message in the text box.
        This method is intended to be invoked remotely."""
        self.display.text.insert(END, message + '\n')


def main(name, room_name='room_1', *args):
    chat = Chatter()
    chat.setup()
    chat.join_room(room_name)
    chat.threadLoop()
    try:
        chat.mainloop()
    except:
        chat.quit()
        (type, value, traceback) = sys.exc_info()
        if type != KeyboardInterrupt:
            raise type, value        

if __name__ == '__main__':
    main(*sys.argv)


