from swampy.Gui import *

class DraggableItem(Item):
    """
    """
    def __init__(self, canvas, tag):
        Item.__init__(self, canvas, tag)
        self.bind('<Button-1>', self.select)
        self.bind('<B1-Motion>', self.drag)
        self.bind('<ButtonRelease-1>', self.drop)

    # the following event handlers take an event object as a parameter

    def select(self, event):
        """select this item for dragging"""
        self.set_drag(event)
        
    def drag(self, event):
        """move this item using the pixel
        coordinates in the event object."""
        # see how far we have moved
        dx, dy = self.sub_drag(event)

        # save the current drag coordinates
        self.set_drag(event)

        # move the item and its handles
        self.move(dx, dy)

    def drop(self, event):
        """drop this item"""


    # the following methods are for dealing with events and drag
    # coordinates
        
    def set_drag(self, event):
        """store the current drag coordinates"""
        self.dragx = event.x
        self.dragy = event.y

    def sub_drag(self, event):
        """subtract d2 from the drag coordinates in event"""
        return event.x - self.dragx, event.y - self.dragy
        

class Hello(Gui):
    def __init__(self):
        Gui.__init__(self)
        self.ca_width = 400
        self.ca_height = 400
        self.setup()

    def setup(self):        
        self.canvas = self.ca(width=self.ca_width, height=self.ca_height,
                              bg='white')

    def text(self):
        font = ('Helvetica', 36)
        item = self.canvas.text([0, 0], 'Hello', font=font, fill='blue')
        item = DraggableItem(item.canvas, item.tag)

    def circle(self):
        item = self.canvas.circle([0, 0], 100, 'yellow')
        item = DraggableItem(item.canvas, item.tag)


if __name__ == '__main__':
    h = Hello()
    h.circle()
    h.text()
    h.mainloop()
