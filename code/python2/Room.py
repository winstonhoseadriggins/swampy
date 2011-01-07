from RemoteObject import *
from threading import *

def run_in_thread(function, *args):
    thread = Thread(target=function, args=args)
    thread.start()
    return thread

class Room(RemoteObject):
    err1 = 'the Room was not able to look up the chatter name you provided'

    def __init__(self, room_name='room_1'):
        RemoteObject.__init__(self)
        self.name = room_name
        self.chatters = {}

        # register with the name server
        self.ns = NameServer()
        try:
            self.connect(self.ns, self.name)
        except Pyro.errors.NamingError:
            print "Couldn't register the name " + self.name
            sys.exit()

    def join(self, chatter_name):
        """add a Chatter to the Room.
        This method is meant to be invoked remotely."""
        print 'Adding %s to %s' % (chatter_name, self.name)
        try:
            # get a proxy for the new Chatter
            chatter = self.ns.get_proxy(chatter_name)
        except:
            raise NameError, Room.err1

        self.chatters[chatter_name] = chatter

    def unjoin(self, chatter_name):
        """Remove a Chatter from the Room """
        print 'Removing %s from %s' % (chatter_name, self.name)
        try:
            del self.chatters[chatter_name]
        except:
            print 'huh'

    def send_message(self, message):
        """send a message to all the Chatter in the room
        This method is meant to be invoked remotely."""
        print 'Broadcasting message: %s' % message
        self.broadcast(message)

    def broadcast(self, message):
        """send a message to all the Chatters, creating one
        thread for each message."""
        for (name, chatter) in self.chatters.items():
            run_in_thread(self.send_one_message, message, name)

    def send_one_message(self, message, name):
        """send a message to the given Chatter"""
        try:
            print name
            self.chatters[name].display_message(message)
        except:
            # if something goes wrong, remove the bad Chatter
            (type, value, traceback) = sys.exc_info()
            print '%s failure...%s, %s' % (name, type, value)
            self.unjoin(name)

def main(name, room_name='room_1', *args):
    room = Room(room_name)
    room.requestLoop()

if __name__ == '__main__':
    main(*sys.argv)

