from World import *

class MyGui(Gui):
    def setup(self):
        self.fr(TOP)
        self.canvas = self.ca(width=400, height=400, bg='white')
        self.endfr()

        self.fr(TOP)
        options = dict(text='hello', width=5)
        en = self.en(LEFT, **options)
        self.bu(LEFT, text='Press me', command=Callable(self.press, en))
        self.bu(LEFT, text='Quit', command=self.quit)
        self.endfr()

    def press(self, *args):
        text = args[0].get()
        self.canvas.text([0, 0], text)

class YourGui(MyGui):
    def setup(self):
        MyGui.setup(self)
        self.color = StringVar()
        self.fr(TOP)
        for color in ['red', 'green', 'blue']:
            self.rb(LEFT, text=color, variable=self.color, value=color)
        self.endfr()

if __name__ == '__main__':
    m = YourGui(debug=True)
    m.setup()
    m.mainloop()
