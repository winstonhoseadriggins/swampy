#!/usr/bin/python

from Gui import *
import string
from time import sleep

class Annike(Gui):

    def __init__(self):
        Gui.__init__(self)
        self.ca_width = 1280
        self.ca_height = 1024
        self.transforms = [ CanvasTransform(self.ca_width, self.ca_height) ]
        sizes = range(100, 800, 100)
        self.fonts = [('Courier', x) for x in sizes]
        self.color = 'blue'
        self.cd = dict(a='aquamarine', d='black', e='black', f='ForestGreen', i='black', j='black', r='red', o='orange', y='yellow', b='blue',
                       g='green', p='purple', q='black', c='chartreuse', h='honeydew', k='khaki', l='lavender', m='maroon', n='navy', s='salmon', t='turquoise', u='black', v='violet', w='wheat', x='black', z='LawnGreen')
        self.letter = None
        self.letters = (string.uppercase + string.lowercase +
                        string.digits + string.punctuation)
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
        if event.char not in self.letters: return

        c = event.char.lower()
        if c in self.cd:
            self.color = self.cd[c]

        self.letter = event.char


    def background(self): 
        mid = [0,100]
        while True:
            while self.letter == None:
                sleep(0.1)
            letter = self.letter
            self.letter = None
            
            for font in self.fonts:
                if self.letter != None: break
                
                if self.tag:
                    self.canvas.delete(self.tag)
                self.tag = self.canvas.text(mid, letter, anchor=CENTER,
                                            fill=self.color, font=font)
                sleep(0.1)

        
if __name__ == '__main__':

    Watcher()

    # create the GUI
    h = Annike()

    # wait for user events
    h.mainloop()
