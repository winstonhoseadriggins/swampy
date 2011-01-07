#!/usr/local/bin/python

# A Python example of drag and drop functionality within a single Tk widget.
# The trick is in the bindings and event handler functions.
# Tom Vrankar twv at ici.net
# translated into Software Design style by Allen Downey


from Gui import *

class Canvas(Gui):
    def __init__ (self):
        Gui.__init__(self)
        self.ca_width = 400
        self.ca_height = 400
        self.itemcolor = 'red'
        self.setup()

    def setup(self):
        self.canvas = self.ca(width=self.ca_width, height=self.ca_height,
                              bg='white')
 
        self.loc = self.dragged = 0
        font = ("Helvetica", 14)
        options = dict(font=font, tags="draggable", fill=self.itemcolor)
        
        self.canvas.text([30, 25], "Item 1", **options)
        self.canvas.text([75, 75], "Item 2", **options)
        self.canvas.text([125, 125], "Item 3", **options)
        self.canvas.text([175, 175], "Item 4", **options)

        self.canvas.tag_bind("draggable", "<ButtonPress-1>", self.down)
        self.canvas.tag_bind("draggable", "<ButtonRelease-1>", self.chkup)
        self.canvas.tag_bind("draggable", "<Enter>", self.enter)
        self.canvas.tag_bind("draggable", "<Leave>", self.leave)

    def down (self, event):
        print "Click on %s" % event.widget.itemcget(CURRENT, "text")
        self.loc = 1
        self.dragged = 0
        event.widget.bind("<Motion>", self.motion)

    def motion (self, event):
        self.config (cursor ="exchange")
        event.widget.itemconfigure (CURRENT, fill ="blue")
        #event.widget.unbind ("<Motion>")
  
    def leave (self, event):
        self.loc = 0

    def enter (self, event):
        self.loc = 1
        if self.dragged == event.time:
            self.up (event)

    def chkup (self, event):
        self.config (cursor ="")
        self.target = event.widget.find_withtag (CURRENT)
        event.widget.itemconfigure (CURRENT, fill=self.itemcolor)
        if self.loc: # is button released in same widget as pressed?
            self.up (event)
        else:
            self.dragged =event.time

    def up (self, event):
        event.widget.unbind ("<Motion>")
        if (self.target == event.widget.find_withtag (CURRENT)):
            print "Select %s" %event.widget.itemcget (CURRENT, "text")
        else:
            event.widget.itemconfigure (CURRENT, fill ="blue")
            self.master.update()
            time.sleep (.1)
            print "%s Drag-N-Dropped onto %s" \
                  %(event.widget.itemcget (self.target, "text"),
                    event.widget.itemcget (CURRENT, "text"))
            event.widget.itemconfigure (CURRENT, fill =self.defaultcolor)


if __name__ == '__main__':
    h = Canvas()
    h.mainloop()
