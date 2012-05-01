from swampy.Gui import *

class DraggableItem(Item):
    """
    """
    def __init__(self, canvas, tag):
        Item.__init__(self, canvas, tag)
        self.handles = []
        self.bind('<Button-1>', self.select)
        self.bind('<B1-Motion>', self.drag)
        self.bind('<ButtonRelease-1>', self.release)

    def show_handles(self):
        """draw handles for this item (if necessary)"""
        if self.handles: return
        
        coords = self.coords()
        print coords
        for i in range(len(coords)):
            tag = self.canvas.circle(coords[i], 5, fill='yellow')
            handle = Handle(self.canvas, tag, self, i)
            self.handles.append(handle)

    # the following event handlers take an event object as a parameter

    def select(self, event):
        print 'Item.select', self
        self.config(fill='red')
        self.set_drag(event)
        self.show_handles()
        
    def drag(self, event):
        """move this item (and its handles) using the pixel
        coordinates in the event object."""

        # see how far we have moved
        dx, dy = self.sub_drag(event, self.drag)

        # save the current drag coordinates
        self.set_drag(event)

        # move the item and its handles
        self.move(dx, dy)
        for handle in self.handles:
            handle.move(dx, dy)

        return dx, dy

    def release(self, event):
        print 'Item.release', self
        self.config(fill='blue')


    # the following methods are for dealing with events and drag
    # coordinates
        
    def get_drag(self, event):
        """get the drag coordinates from this event and translate
        them into canvas coordinates"""
        #x, y = self.canvas.trans([event.x, event.y])
        x, y = event.x, event.y
        return x, y

    def set_drag(self, event):
        """store the current drag coordinates"""
        self.drag = self.get_drag(event)

    def sub_drag(self, event, d2):
        """subtract d2 from the drag coordinates in event"""
        d1 = self.get_drag(event)
        return d1[0] - d2[0], d1[1] - d2[1]
        

class Handle(DraggableItem):
    def __init__(self, canvas, tag, item, index):
        DraggableItem.__init__(self, canvas, tag)
        self.item = item
        self.index = index

    def select(self, event):
        self.set_drag(event)
        
    def drag(self, event):
        """this method is relatively elegant, but it is based on
        assumptions about the way the canvas works that turn out
        not to be true.  So it has an annoying behavior for
        ovals and rectangles.

        To do this right, you probably have to customize the
        behavior of different items (this version probably works
        for polylines, but not ovals and rectangles)."""

        # get the center of this item's bbox and replace the
        # corresponding coordinate of the associated object
        center = self.bbox().center()
        print center

        # move the handle
        dx, dy = DraggableItem.drag(self, event)

        # move the coordinate that corresponds to this handle
        self.item.replace_coord(self.index, center)

    def release(self, event):
        """override Item.release and do nothing"""


class Hello(Gui):
    def __init__(self):
        Gui.__init__(self)
        self.ca_width = 400
        self.ca_height = 400
        self.setup()

    def setup(self):
        self.canvas = self.ca(width=self.ca_width, height=self.ca_height,
                              bg='white')
        self.canvas.bind('<Button-1>', self.click)

        self.row([1,1,1])
        self.bu(text='Hello', command=self.hello)
        self.bu(text='Circle', command=self.circle)
        self.bu(text='Quit', command=self.quit)
        self.endrow()
   
    def hello(self):
        font = ('Helvetica', 36)
        item = self.canvas.text([0, 0], 'Hello', font=font, fill='blue')
        item = DraggableItem(item.canvas, item.tag)

    def circle(self):
        item = self.canvas.circle([0, 0], 100, 'yellow')
        item = DraggableItem(item.canvas, item.tag)

    def click(self, event):
        """this event handler gets invoked when the user clicks
        on the canvas."""
        print 'Hello.click', event.type, event.num, event.x, event.y


if __name__ == '__main__':
    h = Hello()
    h.mainloop()
