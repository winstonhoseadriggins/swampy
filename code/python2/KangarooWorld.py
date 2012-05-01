from swampy.Gui import Gui

import Lumpy
lumpy = Lumpy.Lumpy()
lumpy.make_reference()

class World(Gui):
    def __init__(self):
        Gui.__init__(self)      # invoke the init method from the parent
        self.animals = []

    def register(self, animal):
        self.animals.append(animal)

class Animal(object):
    def __init__(self, world):
        self.world = world
        world.register(self)

class Kangaroo(Animal):
    def __init__(self, world):
        Animal.__init__(self, world)   # invoke the init method from the parent
        self.pouch = []

world = World()

kanga = Kangaroo(world)
roo = Kangaroo(world)

kanga.pouch.append(roo)

lumpy.object_diagram()
lumpy.class_diagram()
