from Tkinter import *

def hello(event):
    print 'hello'

root = Tk()
canvas = Canvas(root)
canvas.pack()

tag = 'tag'
canvas.tag_bind(tag, "<ButtonPress-1>", hello)
canvas.create_text(100, 100, text='hello', tags=tag)

root.mainloop()





