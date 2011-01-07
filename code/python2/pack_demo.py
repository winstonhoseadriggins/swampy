from Gui import *

#---------------------------
print 'Figure 17.3 a'

g = Gui()
b1 = g.bu(LEFT, text='OK', command=g.quit)
b2 = g.bu(LEFT, text='Cancel')
b3 = g.bu(LEFT, text='Help')

g.mainloop()

#---------------------------
print 'Figure 17.3 b'

b2.configure(text='Cancel Command')

g.mainloop()

#---------------------------
print 'Figure 17.3 c'

for b in [b1, b2, b3]:
    b.pack(side=TOP)

g.mainloop()
g.destroy()

#---------------------------
print 'Figure 17.4 a'

g = Gui()
options = dict(side=LEFT, padx=10, pady=10)
b1 = g.bu(text='OK', command=g.quit, **options)
b2 = g.bu(text='Cancel', **options)
b3 = g.bu(text='Help', **options)

g.mainloop()

#---------------------------
print 'Figure 17.4 b'

options = dict(side=LEFT, padx=0, pady=0, ipadx=10, ipady=10)
for b in [b1, b2, b3]:
    b.pack(**options)

g.mainloop()

#---------------------------
print 'Figure 17.4 c'

options = dict(side=LEFT, padx=10, pady=10, ipadx=10, ipady=10)
for b in [b1, b2, b3]:
    b.pack(**options)

g.mainloop()
g.destroy()

#---------------------------
print 'Figure 17.5'

g = Gui()
options = dict(side=TOP, fill=X)
b1 = g.bu(text='OK', command=g.quit, **options)
b2 = g.bu(text='Cancel Command', **options)
b3 = g.bu(text='Help', **options)

g.mainloop()
g.destroy()

#---------------------------
print 'Figure 17.6'

g = Gui()
options = dict(side=TOP, fill=X)

# create the widgets
g.fr()
la = g.la(TOP, text='List of colors:')
lb = g.lb(LEFT)
sb = g.sb(RIGHT, fill=Y)
g.endfr()

bu = g.bu(BOTTOM, text='OK', command=g.quit)

# fill the listbox with color names
fp = open('/usr/X11R6/lib/X11/rgb.txt')
fp.readline()

for line in fp:
    t = line.split('\t')
    name = t[2].strip()
    lb.insert(END, name)


# tell the listbox and the scrollbar about each other
lb.configure(yscrollcommand=sb.set)
sb.configure(command=lb.yview)

g.mainloop()
g.destroy()


#---------------------------
print 'Figure 17.7 a'

g = Gui()
options = dict(side=LEFT)
b1 = g.bu(text='OK', command=g.quit, **options)
b2 = g.bu(text='Cancel', **options)
b3 = g.bu(text='Help', **options)

g.geometry('300x150')
g.mainloop()


#---------------------------
print 'Figure 17.7 b'

def pack(**options):
    for b in [b1, b2, b3]:
        b.pack(**options)

pack(side=LEFT, fill=X, expand=1)

g.mainloop()

#---------------------------
print 'Figure 17.7 c'

options = dict(side=LEFT, fill=NONE, expand=0)
b1.pack(**options)
b2.pack(**options)

# the override function is defined in Gui.py
override(options, expand=1)
b3.pack(**options)

g.mainloop()

#---------------------------
print 'Figure 17.7 d'

pack(**options)

g.mainloop()

#---------------------------
print 'Figure 17.7 e'

options = dict(side=LEFT, fill=BOTH, expand=1)
pack(**options)

g.mainloop()
