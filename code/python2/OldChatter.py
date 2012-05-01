#!/usr/bin/python

from Tkinter import *
from swampy.Gui import *
import sys
import random
import Pyro.core
import Pyro.util
import Pyro.naming
from RemoteObject import *

class Chatter(Gui):
    def __init__(self, channel='1'):
        Gui.__init__(self)
        self.name = 'sd_chatter%d' % random.randint(0, 1000000)
        print self.name
        self.setup()
        channel_name = 'sd_chat_channel_' + channel
        self.connect(channel_name)

    def setup(self):
        self.display = self.te()

        self.fr(TOP, fill=X, expand=1)
        self.entry = self.en(LEFT, fill=X, expand=1)
        self.bu(LEFT, text='Send', command=self.send)
        self.bu(LEFT, text='Quit', command=self.quit)
        self.endfr()

    def quit(self):
        self.receiver.stopLoop()
        Gui.quit(self)

    def send(self):
        message = self.entry.get()
        self.c.broadcast(message)

    def insert(self, message):
        self.display.insert(END, message)

    def connect(self, name):
        try:
            self.c = get_remote_object(name)
        except Pyro.errors.NamingError:
            print 'Could not find a coordinator named', name
            sys.exit()

        # create the Receiver, start it, and register it
        self.receiver = Receiver(self)
        self.receiver.threadLoop()        
        self.c.register(self.receiver.uri)


class Receiver(RemoteObject):
    def __init__(self, chat, name=None):
        self.chat = chat
        self.name = name
        if self.name == None:
            self.name = 'sd_chatter_%d' % random.randint(0, 1000000) 
        RemoteObject.__init__(self, self.name)
    
    def post_message(self, message):
        self.chat.insert(str(message))


def main(name, channel='1', *args):
    chat = Chatter(channel)
    chat.mainloop()

if __name__ == '__main__':
    main(*sys.argv)


