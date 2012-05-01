from swampy.TurtleWorld import *
world = TurtleWorld()    

bob = Turtle()

def square(turtle):
    for i in range(4):
        fd(turtle, 100)
        lt(turtle)

square(bob)

wait_for_user()
