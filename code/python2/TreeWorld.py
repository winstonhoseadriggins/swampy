#!/usr/bin/python

from World import *

class TreeWorld(Gui):

    def __init__(self):
        Gui.__init__(self)
        self.ca_width = 600
        self.ca_height = 600
        #self.transforms = [ CanvasTransform(self.ca_width, self.ca_height) ]
        self.setup()


    # setup creates the GUI elements (called widgets)
    def setup(self):
        
        # left frame
        self.fr(LEFT)
        self.canvas = self.ca(width=self.ca_width, height=self.ca_height,
                              bg='white')
        self.endfr()

        # right frame
        self.fr(LEFT, fill=BOTH, expand=1)
        # no buttons
        self.endfr()


    def example_code(self):
        # put some text on the canvas
        item = self.canvas.text([0,0], 'hello', 'red', tags='stack1')
        item = self.canvas.text([0,-10], 'world', 'red', tags='stack1')

        # find the bounding box of the text
        bbox = self.canvas.bbox('stack1')
        print bbox
        width = bbox[1][0] - bbox[0][0]
        print width

        # draw a rectangle around the text
        self.canvas.rectangle(bbox)

        # draw a line connecting this node to another
        p1 = bbox.midright()
        print p1
        p2 = Pos(p1)
        p2[0] += 50
        self.canvas.line([p1, p2])
    
if __name__ == '__main__':

    # create the GUI
    h = TreeWorld()
    h.example_code()
    
    # wait for user events
    h.mainloop()
