import pylab
xs = range(0, 10)
ys = [x**2 for x in xs]
pylab.plot(xs, ys, '-ro')
pylab.title('Parabola')
pylab.xlabel('x')
pylab.ylabel('y = x**2')
pylab.show()
