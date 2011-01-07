"""

Solution to an exercise from
Think Python: An Introduction to Software Design
Allen B. Downey

This program requires Gui.py, which is part of
Swampy; you can download it from thinkpython.com/swampy.

This program started with a recipe by Noah Spurrier at
http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/521918

"""

import os, sys
import Image as PIL
import ImageTk
import Tkinter

class ImageBrowser(Tkinter.Tk):
    """An image browser read the files in a given directory and
    displays any images that can be read by PIL.

    The user clicks on image to go to the next.
    """

    def __init__(self):
        Tkinter.Tk.__init__(self)
        self.label = Tkinter.Label(self)
        self.label.pack()
        self.label.bind('<Button>', self.exit_mainloop)

    def exit_mainloop(self, event):
        """Tk.quit exits from mainloop"""
        self.quit()
        
    def image_loop(self, dirname='.'):
        """loop through the files in the directory, displaying
        images and skipping files PIL can't read.
        """
        files = os.listdir(dirname)
        for file in files:
            try:
                self.show_image(file)
                self.mainloop()
            except IOError:
                continue
            except:
                return

    def show_image(self, filename):
        """Use PIL to read the file and ImageTk to convert
        to a PhotoImage, which Tk can display.
        """
        image = PIL.open(filename)
        self.tkpi = ImageTk.PhotoImage(image)
        self.label.config(image=self.tkpi)

def main(script, dirname='.'):
    g = ImageBrowser()
    g.image_loop(dirname)
        
if __name__ == '__main__':
    main(*sys.argv)
