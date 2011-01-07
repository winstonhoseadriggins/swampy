import visual
import pylab

xs = pylab.linspace(0, 1, 11)

for r in xs:
    for g in xs:
        for b in xs:
            visual.sphere(pos=(r, g, b), radius=0.04, color=(r, g, b))
