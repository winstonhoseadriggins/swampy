#!/usr/bin/python

from Gui import *
from time import sleep

class Table(Gui):
    """A Table displays a green canvas and a control area.
    By default, all tables share a common deck."""
    def __init__(self, dir):
        Gui.__init__(self)
        self.dir = dir
        self.cardset = {}
        self.setup()
        

    def setup(self):
        self.ca_width = 500
        self.ca_height = 400
        
        # left frame
        self.fr(LEFT)
        self.canvas = self.ca(width=self.ca_width, height=self.ca_height,
                              bg='dark green', transforms=[])
        self.endfr()

        # right frame
        self.fr(LEFT, fill=BOTH, expand=1)
        self.bu(TOP, text='Quit', command=self.quit)
        self.bu(TOP, text='Deal', command=self.deal)
        self.bu(TOP, text='Print', command=self.canvas.dump)
        self.endfr()

    def deal(self, ext='gif'):
        """deal the cards and display them on the canvas,
        storing the Hands and HandViews in self.views"""
        suits = 'cdhs'
        for rank in range(1,14):
            for suit in range(4):
                filename = '%s/%.2d%s.%s' % (self.dir, rank, suits[suit], ext)
                image = PhotoImage(file='danger.gif')
                self.cardset[suit,rank] = image

        image = PhotoImage(file='danger.gif')
        self.z = image

        for rank in range(1,14):
            for suit in range(4):
                #image = self.cardset[suit,rank]
                print image
                x, y = rank * 30, suit * 60
                self.canvas.image([x, y], image, anchor=NW)
                

def main(name, cardstyle='tuxedo', *args):
    table = Table('poker/cardsets/cardset-' + cardstyle)
    #table.read_cards()
    table.mainloop()
    
if __name__ == '__main__':
    main(*sys.argv)


