import sys, random, string
from Heap import Heap

length = 100         # length of plank in meters
speed = 1            # pirate walking speed in meters per second
npirates = 10         # number of pirates
gtime = 0             # global clock

def ids():
    for c in string.uppercase:
        yield c
idlist = ids()

class Pirate:
    """a pirate has a position, direction and speed
    """
    def __init__(self):
        self.id = idlist.next()
        self.position = random.uniform(0, length)
        self.direction = random.choice([-1, 1])
        self.speed = speed

    def move(self, dt):
        """move the pirate the distance he moves in time dt"""
        self.position += self.direction * self.speed * dt

    def predict_fall(self):
        """predict when this pirate will fall off the plank (assuming
        no collisions) and return an event object
        """
        if self.direction == -1:
            d = self.position
        else:
            d = length - self.position
        dt = d / self.speed
        e = make_fall(gtime+dt, self)
        return e

    def __str__(self):
        return 'Pirate %s at position %.4g' % (self.id,
                                               self.position * self.direction)

# list of pirates
pirates = [Pirate() for p in range(npirates)]

# event queue
heap = Heap()

class Event(list):
    """An Event object is a list with one element, the time
    at which the event occurs.  Event objects also have an
    attribute named handle which is a reference to the method
    that will be used to handle the event.
    """
    def __init__(self, time):
        self.append(time)

    # time is stored as the first element of the list, but
    # can be accessed as if it were an instance variable.
    def get_time(self): return self[0]
    def set_time(self, t): self[0] = t
    time = property(get_time, set_time)

    # the following methods are event handlers
    
    def handle_fall(self):
        p = self.pirate
        print p, 'falls at time', gtime
        pirates.remove(p)


def make_fall(time, pirate):
    """return a new fall Event with the given time and pirate
    """
    e = Event(time)
    e.pirate = pirate
    e.handle = e.handle_fall
    return e


def main(name, *args):
    global gtime

    # initialize the heap with one event per pirate
    for p in pirates:
        print p
        e = p.predict_fall()
        heap.push(e)

    # main loop
    while heap:

        # get the next event
        e = heap.popmin()

        # move all the pirates
        dt = e.time - gtime        
        for p in pirates:
            p.move(dt)

        # update the global clock and handle the event
        gtime = e.time
        e.handle()
    
    print 'Last pirate fell at time', gtime
    print pirates

if __name__ == '__main__':
    main(*sys.argv)
