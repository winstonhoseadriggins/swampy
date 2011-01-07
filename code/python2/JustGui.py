# Gui provides wrappers for many of the methods in the Tk
# class; also, it keeps track of the current frame so that
# you can create new widgets without naming the parent frame
# explicitly.

class Gui(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.frame = self          # the current frame
        self.frames = []           # the stack of nested frames

    # frame
    def fr(self, side=TOP, fill=NONE, expand=0, anchor=CENTER, **options):
        # save the current frame, then create the new one
        self.frames.append(self.frame)
        if debug:
            options['bd'] = 5
            options['relief'] = RIDGE
        self.frame = self.widget(Frame, side, fill, expand, anchor, **options)
        return self.frame

    # end frame
    def endfr(self):
        self.frame = self.frames.pop()

    # top level window
    def tl(self, side=TOP, fill=NONE, expand=0, anchor=CENTER, **options):
        # push the current frame, then create the new one
        self.frames.append(self.frame)
        self.frame = Toplevel(options)
        return self.frame

    # canvas
    def ca(self, side=TOP, fill=NONE, expand=0, anchor=CENTER, **options):
        return self.widget(Canvas, side, fill, expand, anchor, **options)

    # label
    def la(self, side=TOP, fill=NONE, expand=0, anchor=CENTER, **options):
        return self.widget(Label, side, fill, expand, anchor, **options)

    # button
    def bu(self, side=TOP, fill=NONE, expand=0, anchor=CENTER, **options):
        return self.widget(Button, side, fill, expand, anchor, **options)

    # menu button
    def mb(self, side=TOP, fill=NONE, expand=0, anchor=CENTER, **options):
        mb = self.widget(Menubutton, side, fill, expand, anchor,
                         **options)
        mb.menu = Menu(mb, relief=SUNKEN)
        mb['menu'] = mb.menu
        return mb

    # menu item
    def mi(self, mb, label='', **options):
        mb.menu.add_command(label=label, **options)        

    # entry
    def en(self, side=TOP, fill=NONE, expand=0, anchor=CENTER,
           text='', **options):
        en = self.widget(Entry, side, fill, expand, anchor, **options)
        en.insert(0, text)
        return en

    # text entry
    def te(self, side=TOP, fill=NONE, expand=0, anchor=CENTER, **options):
        return self.widget(Text, side, fill, expand, anchor, **options)

    # this is the mother of all widget constructors.  the constructor
    # argument is the function object that will be called to build
    # the new widget
    def widget(self, constructor,
               side=TOP, fill=NONE, expand=0, anchor=CENTER, **options):
        widget = constructor(self.frame, options)
        widget.pack(side=side, fill=fill, expand=expand, anchor=anchor)
        return widget

    # the following are wrappers on the tk canvas items

    def create_circle(self, x, y, r, fill='', **options):
        options['fill'] = fill
        coords = self.trans([[x-r, y-r], [x+r, y+r]])
        tag = self.canvas.create_oval(coords, options)
        return tag;
    
    def create_oval(self, coords, fill='', **options):
        options['fill'] = fill
        return self.canvas.create_oval(self.trans(coords), options)

    def create_rectangle(self, coords, fill='', **options):
        options['fill'] = fill
        return self.canvas.create_rectangle(self.trans(coords), options)

    def create_line(self, coords, fill='black', **options):
        options['fill'] = fill
        tag = self.canvas.create_line(self.trans(coords), options)
        return tag
    
    def create_polygon(self, coords, fill='', **options):
        options['fill'] = fill
        return self.canvas.create_polygon(self.trans(coords), options)

    def create_text(self, coord, text='', fill='black', **options):
        options['text'] = text
        options['fill'] = fill
        return self.canvas.create_text(self.trans([coord]), options)

    def create_image(self, coord, image, **options):
        options['image'] = image
        return self.canvas.create_image(self.trans([coord]), options)

    def itemconfig(self, tag, **options):
        self.canvas.itemconfig(tag, options)

    def itemcget(self, tag, option):
        return self.canvas.itemcget(tag, option)

    def delete_item(self, tag):
        self.canvas.delete(tag)

    def move_item(self, tag, dx, dy):
        self.canvas.move(tag, dx, dy)

    def print_canvas(self, filename='gui.eps'):
        ps = self.canvas.postscript()
        fp = open(filename, 'w')
        fp.write(ps)
        fp.close()

    def trans(self, coords):
        for trans in self.transforms:
            coords = trans.trans_list(coords)
        return coords

