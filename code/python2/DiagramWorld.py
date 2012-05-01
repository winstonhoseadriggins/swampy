from swampy.World import *
import StateDiag

world = TurtleWorld()
diag = StateDiag.Diagram()
diag.opaque_class(World)
diag.opaque_class(TurtleWorld)

bob = Turtle(world)
diag.draw_snapshot()

# wait for the user to do something
world.mainloop()


