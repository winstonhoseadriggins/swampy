#!/usr/local/bin/python

# A Python example of drag and drop functionality within a single Tk widget.
# The trick is in the bindings and event handler functions.
# Tom Vrankar twv at ici.net
# translated into Software Design style by Allen Downey

# empirical events between dropee and target, as determined from Tk 8.0
# down.
# leave.
# up, leave, enter.

from Gui import *

class Canvas(Gui):
    def __init__ (self):
        Gui.__init__(self)
        self.ca_width = 400
        self.ca_height = 400
        self.transforms = [ CanvasTransform(self.ca_width, self.ca_height) ]
        self.setup()

    def setup(self):
        self.canvas = self.ca(width=self.ca_width, height=self.ca_height,
                              bg='white')
 
        self.loc = self.dragged = 0
        self.defaultcolor = self.canvas.itemcget(
            self.canvas.create_text (30, 25,
            font =("Helvetica", 14), text ="Item 1", tags ="DnD"), "fill")
        self.canvas.create_text (75, 75,
            font =("Helvetica", 14), text ="Item 2", tags ="DnD")
        self.canvas.create_text (125, 125,
            font =("Helvetica", 14), text ="Item 3", tags ="DnD")
        self.canvas.create_text (175, 175,
            font =("Helvetica", 14), text ="Item 4", tags ="DnD")
        self.canvas.create_text (225, 225,
            font =("Helvetica", 14), text ="Item 5", tags ="DnD")

        self.canvas.tag_bind ("DnD", "<ButtonPress-1>", self.down)
        self.canvas.tag_bind ("DnD", "<ButtonRelease-1>", self.chkup)
        self.canvas.tag_bind ("DnD", "<Enter>", self.enter)
        self.canvas.tag_bind ("DnD", "<Leave>", self.leave)

    def down (self, event):
        print "Click on %s" %event.widget.itemcget (CURRENT, "text")
        self.loc =1
        self.dragged =0
        event.widget.bind ("<Motion>", self.motion)

    def motion (self, event):
        self.config (cursor ="exchange")
        event.widget.itemconfigure (CURRENT, fill ="blue")
        event.widget.unbind ("<Motion>")
  
    def leave (self, event):
        self.loc =0

    def enter (self, event):
        self.loc =1
        if self.dragged ==event.time:
            self.up (event)

    def chkup (self, event):
        self.config (cursor ="")
        self.target = event.widget.find_withtag (CURRENT)
        event.widget.itemconfigure (CURRENT, fill =self.defaultcolor)
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
