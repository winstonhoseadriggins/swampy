import Pyro.core
import Pyro.util
import Pyro.naming
from RemoteObject import *

# A Subject is an object that keeps track of the Observers
# watching it.  When the state of a subject changes, it
# notifies each Observer on the list.
class Subject(RemoteObject):
    def __init__(self, name):
        RemoteObject.__init__(self, name)
        self.observers = []

    def register(self, name):
    # register a new Observer
        observer = get_remote_object(name)
        self.observers.append(observer)

    def notify_observers(self):
    # notify all registered observers when the state of the subject changes
        for observer in self.observers:
            print 'Notifying', observer
            try:
                observer.notify()
            except:
                pass

class SimpleSubject(Subject):
    def __init__(self, name, state=0):
        Subject.__init__(self, name)
        self.state = 0
        
    def set_state(self, state):
    # change the state of the Subject
        print 'New state', state
        self.state = state
        run_in_thread(self.notify_observers)

    def get_state(self):
    # get the current state of the Subject
        return self.state

def run_in_thread(function, *args):
    thread = Thread(target=function, args=args)
    thread.start()
    return thread
 
def main(script, name='bob', *args):
    SimpleSubject(name).requestLoop()
    
if __name__ == '__main__':
    main(*sys.argv)
import Pyro.core
import Pyro.util
import Pyro.naming
from RemoteObject import *
import random
from time import sleep

# An Observer is an object that watches another object and reacts
# whenever the Subject changes state.
class Observer(RemoteObject):
    def __init__(self, subject_name):

        # choose a name and initialize the RemoteObject
        self.name = subject_name + '_observer%d' % random.randint(0, 1000000)
        RemoteObject.__init__(self, self.name)

        # register with the subject
        self.subject = get_remote_object(subject_name)
        self.subject.register(self.name)
        print "I just registered."

    def notify(self):
    # when the subject is modified, it invokes notify
        state = self.subject.get_state()
        print 'Observer notified; new state =', state

def main(script, subject_name='bob', *args):
    Observer(subject_name).requestLoop()

if __name__ == '__main__':
    main(*sys.argv)
import Pyro.core
import Pyro.util
import Pyro.naming
import sys
from RemoteObject import *

class Modifier:
    def __init__(self, subject_name):
        self.subject = get_remote_object(subject_name)

    def modify(self):
    # increment the state of the Subject
        state = self.subject.get_state()
        self.subject.set_state(state+1)

def main(script, subject_name='bob', *args):
    # create a modifier and use it to change the state of the Subject
    modifier = Modifier(subject_name)
    modifier.modify()

if __name__ == '__main__':
    main(*sys.argv)
