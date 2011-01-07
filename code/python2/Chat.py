#!/usr/bin/python

from Tkinter import *
from Gui import *
import sys
import random
import Pyro.core
import Pyro.util
import Pyro.naming
from RemoteObject import RemoteObject

class Chat(Gui):
    def __init__(self, channel='1'):
        Gui.__init__(self)
        self.name = 'sd_chatter%d' % random.randint(0, 1000000)
        print self.name
        self.setup()
        uri = 'PYRONAME://sd_chat_channel_' + channel
        self.connect(uri)

    def setup(self):
        self.col()
        self.display = self.te()

        self.row()
        self.entry = self.en()
        self.bu(text='Send', command=self.send)
        self.bu(text='Quit', command=self.quit)
        self.endrow()

        self.endcol()

    def quit(self):
        self.receiver.stopLoop()
        Gui.quit(self)

    def send(self):
        message = self.entry.get()
        self.c.broadcast(message)

    def insert(self, message):
        self.display.insert(END, message)

    def connect(self, uri):
        Pyro.core.initClient()
        try:
            self.c = Pyro.core.getProxyForURI(uri)
        except Pyro.errors.NamingError:
            print 'Could not find a coordinator named', uri
            sys.exit()

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
    chat = Chat(channel)
    chat.mainloop()

if __name__ == '__main__':
    main(*sys.argv)


