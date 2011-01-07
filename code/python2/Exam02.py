from World import *

class MyGui(Gui):
    def setup(self):
        self.fr(TOP)
        options = dict(side=LEFT, width=5)
        self.en1 = self.en(text='3', **options)
        self.la(LEFT, text='*')
        self.en2 = self.en(text='5', **options)
        self.la(LEFT, text='=')
        self.en3 = self.en(**options)
        self.endfr()

        self.fr(TOP)
        self.bu(LEFT, text='Go', command=self.make_callable())
        self.bu(LEFT, text='Quit', command=self.quit)
        self.endfr()

    def make_callable(self):
        print 'hello'
        return Callable(go, self.en1, self.en2, self.en3)

def get_int(en):
    x = en.get()
    x = int(x)
    print x
    return x

def put_int(en, x):
    en.delete(0, END)
    en.insert(0, str(x))
    
def go(en1, en2, en3):
    a = get_int(en1)
    b = get_int(en2)
    c = a * b
    print c
    put_int(en3, c)

if __name__ == '__main__':
    m = MyGui()
    m.setup()
    m.mainloop()
