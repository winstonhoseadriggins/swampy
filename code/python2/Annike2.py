#!/usr/bin/python

from swampy.Gui import *
import string
from time import sleep

cd = dict(
    a='aquamarine',
    b='blue',
    c='chartreuse',
    d='DodgerBlue3',  #denim
    e='dark violet',  #eggplant
    f='ForestGreen',
    g='green',
    h='MediumOrchid1',  #heliotrope
    i='dark blue',
    j='SeaGreen',   #jade
    k='khaki',
    l='lavender',
    m='maroon',
    n='navy',
    o='orange',
    p='purple',
    q='YellowGreen',   #quince
    r='red',
    s='salmon',
    t='turquoise',
    u='tomato4',   # umber
    v='violet',
    w='hot pink',  # watermelon
    x='black',
    y='yellow',
    z='light green'  # zuccini 
)

allchars = (string.uppercase + string.lowercase +
            string.digits + string.punctuation + string.whitespace)

sizes = range(100, 700, 100)
fonts = [('Courier', x) for x in sizes]

dx = 375
positions = [(x-70, 100) for x in [-dx, 0, dx]]

class Letter:
    def __init__(self, char, color, position):
        self.char = char
        self.color = color
        self.sizeindex = 0
        self.position = position
        self.tag = None

    def step(self, world):
        if self.sizeindex == len(fonts):
            return
        
        if self.tag:
            self.delete(world)
            
        font = fonts[self.sizeindex]
        self.sizeindex += 1
        self.tag = world.canvas.text(self.position, self.char,
                                    fill=self.color, font=font,
                                    anchor=CENTER)
    def delete(self, world):
        world.canvas.delete(self.tag)

class Annike(Gui):
    def __init__(self):
        Gui.__init__(self)
        self.ca_width = 1280
        self.ca_height = 1024
        self.transforms = [ CanvasTransform(self.ca_width, self.ca_height) ]
        self.color = 'blue'
        self.posindex = 0
        self.letters = []
        self.thread = Thread(self.background)
        self.setup()


    # setup creates the GUI elements (called widgets)
    def setup(self):
        
        self.canvas = self.ca(width=self.ca_width, height=self.ca_height,
                              bg='white')
        self.bind('<Key>', self.keystroke)
#        tag = self.canvas.text([0,0], letters, font=self.font)
#        self.canvas.delete(tag)
        self.tag = None
                          
    def keystroke(self, event):
        if event.char == '': return
        if event.char not in allchars: return

        c = event.char.lower()
        if c in cd:
            self.color = cd[c]

        position = positions[self.posindex]
        self.posindex = (self.posindex + 1) % len(positions)

        letter = Letter(event.char, self.color, position)

        if len(self.letters) >= 3:
            old = self.letters.pop(0)
            old.delete(self)
        self.letters.append(letter)


    def background(self): 
        while True:
            for letter in self.letters:
                letter.step(self)
            sleep(0.1)
            

        
if __name__ == '__main__':

    Watcher()

    # create the GUI
    a = Annike()

    # wait for user events
    a.mainloop()
