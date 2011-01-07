import sys, random, string
from Heap import Heap

length = 100         # length of plank in meters
speed = 1            # pirate walking speed in meters per second
npirates = 2         # number of pirates
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
        self.next_event = None

    def move(self, dt):
        """move the pirate the distance he moves in time dt"""
        self.position += self.direction * self.speed * dt

    def set_next_event(self, e):
        """keep track of the next event that pertains to this
        pirate.  If another event preempts the earliest predicted
        event, cancel the preempted event.
        """
        ne = self.next_event
        if ne == None:
            self.next_event = e
        elif ne.time > e.time:
            ne.cancel()
            self.next_event = e

    def make_event(self):
        """return either a collision event or a fall event, depending
        """
        e = self.predict_collision(pirates) or self.predict_fall()
        return e
    
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

    def distance(self, other):
        """return the distance between pirates self and other"""
        return abs(self.position - other.position)

    def predict_collision(self, pirates):
        """predict when this pirate will collide with another and
        return an event object or None
        """
        # find pirates that are in the direction p is facing
        if self.direction == -1:
            others = [(self.distance(other), other) for other in pirates
                      if other.position > self.position]
        else:
            others = [(self.distance(other), other) for other in pirates
                      if other.position < self.position]
        if others == []: return None

        # find the closest pirate and the time until collision
        d, other = min(others)
        if self.direction * other.direction == 1:
            dt = d / (self.speed + other.speed)
        elif self.speed > other.speed:
            dt = d / (self.speed - other.speed)
        else:
            return None

        # make and return the event
        e = make_collision(gtime+dt, self, other)
        return e

    def __str__(self):
        return 'Pirate %s at position %.4g' % (self.id,
                                               self.position * self.direction)

    def arrr(self):
        print self, 'Arrr!'
        self.cancel_events()
        self.direction *= -1
        self.speed = 0

    def resume(self):
        print self, 'resuming!'
        self.speed = speed
        e = self.make_event()
        heap.push(e)

    def cancel_events(self):
        for event in heap:
            if self in event.__dict__.itervalues():
                event.cancel()

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

    def cancel(self):
        self.handle = self.handle_cancelled

    # the following methods are event handlers
    
    def handle_fall(self):
        p = self.pirate
        print p, 'falls at time', gtime
        pirates.remove(p)

    def handle_collision(self):
        print 'Collision at', gtime
        self.p.arrr()
        self.q.arrr()
        self.time += 1.0
        self.handle = self.handle_rebound
        heap.push(self)

    def handle_rebound(self):
        print 'Rebound at', gtime
        self.p.resume()
        self.q.resume()

    def handle_cancelled(self):
        print 'Cancelled event', gtime


def make_fall(time, pirate):
    """return a new fall Event with the given time and pirate
    """
    e = Event(time)
    e.pirate = pirate
    e.handle = e.handle_fall
    pirate.set_next_event(e)
    return e

def make_collision(time, p, q):
    """return a new collision Event with the given time,
    and pirates p and q
    """
    e = Event(time)
    e.p = p
    e.q = q
    e.handle = e.handle_collision
    p.set_next_event(e)
    q.set_next_event(e)
    return e

def main(name, *args):
    global gtime

    # initialize the heap with one event per pirate
    for p in pirates:
        e = p.make_event()
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
