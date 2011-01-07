from Gui import *

def callback(event):
    print event
    return 'break'

g = Gui()
entry = g.en()
entry.bind('<Any-Key>', callback)
g.mainloop()

