from Gui import *
from sd_hw03_soln import *

class Rotate(Gui):

    def __init__(self):
        Gui.__init__(self)
        self.setup()
        self.mainloop()

    def setup(self):
        # text entries
        self.entry1 = self.en()
        self.entry2 = self.en()

        # label
        self.label = self.la()

        # buttons
        self.gr(2, [1,1])
        self.bu(text='Rotate', command=self.rotate_entry)
        self.bu(text='Quit', command=self.quit)
        self.endgr()

    def rotate_entry(self):
        # get the contents of the entries
        word = self.entry1.get()
        shift = self.entry2.get()
        shift = int(shift)           # convert string to int

        # post the result
        result = rotate_word(word, shift)
        self.label.configure(text=result)

if __name__ == '__main__':
    Rotate()
