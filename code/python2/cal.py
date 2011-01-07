from pyx import *
from datetime import *

names = ['Sun','Mon','Tues','Wed','Thurs','Fri','Sat']

def draw_entry(c, y, d):
    cell = height
    width = 20.0

    cc = canvas.canvas()
    c.insert(cc, [trafo.translate(0, y)])

    textstyle = [text.halign.boxleft, text.valign.top]
    cc.text(0.1*cell, 0.9*height, names[d.weekday()], textstyle)
    cc.text(0.1*cell, 0.5*height, str(d.day), textstyle)
    
    cc.stroke(path.rect(0, 0, width, height))
    cc.stroke(path.rect(0, 0, cell, height))
    cc.stroke(path.rect(cell, 0, cell, height))
    cc.stroke(path.rect(2*cell, 0, cell, height))

    dashed = [style.linestyle.dashed]

    n = 6
    for i in range(n):
        y = height * i / n
        cc.stroke(path.line(cell, y, 3*cell, y), dashed)
        if i%2==0:
            cc.stroke(path.line(cell, y, width, y), dashed)

d = date.today()
delta = timedelta(days=1)

height = 1.8
c = canvas.canvas()

draw_entry(c, height*7, d)
draw_entry(c, height*6, d+delta)

c.writeEPSfile("hello")
