from Tkinter import *
tk = Tk()
ca = Canvas(tk, width=500, height=500, )
ca.pack(side=TOP)
ca.create_line([[0, 0], [350, 250]])
tk.mainloop()

