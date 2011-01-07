import Lumpy
lumpy = Lumpy.Lumpy()

# normally class objects are opaque, meaning that Lumpy
# doesn't show their attributes, but you can change this
# behavior with the transparent_class method
clstype = type(Lumpy.Lumpy)
lumpy.transparent_class(clstype)

lumpy.make_reference()

class Kangaroo:
    """a Kangaroo is a marsupial"""
    
    def __init__(self, contents=[]):
        self.pouch_contents = contents

    def put_in_pouch(self, item):
        self.pouch_contents.append(item)

kanga = Kangaroo()
roo = Kangaroo()
kanga.put_in_pouch(roo)

lumpy.object_diagram()

