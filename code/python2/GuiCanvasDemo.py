from swampy.Gui import *

width, height = 500, 500

gui = Gui()

ca = gui.ca(width=width, height=height)
ca.transforms.append(CanvasTransform(width, height))

ca.create_circle(0, 0, 200, 'blue')

font = 'Helvetica', 72
ca.create_text([0, 0], 'Hi, Mark!', 'yellow', font=font)

gui.mainloop()
