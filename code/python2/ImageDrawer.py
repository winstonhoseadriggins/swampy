import Image as PIL
import ImageDraw
import ImageTk
import Gui

class ImageDrawer(Gui.Gui):
    def __init__(self, size, mode='1', color=255):
        self.image = PIL.new(mode, size, color)
        Gui.Gui.__init__(self)
        self.button = self.bu(command=self.quit, relief=Gui.FLAT)
        self.draw = ImageDraw.Draw(self.image)

    def cell(self, i, j, size=1, fill=0):
        x, y = i*size, j*size
        self.draw.rectangle([x, y, x+size, y+size], fill=fill)

    def rectangle(self, x, y, width, height, outline=0):
        self.draw.rectangle([x, y, x+width, y+height], outline=outline)

    def show(self):
        self.tkpi = ImageTk.PhotoImage(self.image)
        self.button.config(image=self.tkpi)
 
    def save(self, filename='image.gif'):
        self.image.save(filename)

if __name__ == '__main__':
    width = 300
    height = 200
    draw = ImageDrawer([width, height])
    draw.cell(10, 10, 2)
    draw.rectangle(0, 0, width-1, height-1)
    draw.show()
    draw.mainloop()
    draw.save()
