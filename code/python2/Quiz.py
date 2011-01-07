import Pyro.core
import Pyro.util
import Pyro.naming
from RemoteObject import *
import random
from time import sleep

# A Subject is an object that keeps track of the Observers
# watching it.  When the state of a subject changes, it
# notifies each Observer on the list.
class Subject(RemoteObject):
    def __init__(self, name):
        RemoteObject.__init__(self, name)
        self.observers = []
    
    def register(self, uri):
        observer = Pyro.core.getProxyForURI(uri)
        self.observers.append(observer)

    def notify_observers(self):
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
        self.requestLoop()
        
    def set_state(self, state):
        print 'New state', state
        self.state = state
        Thread(target=self.notify_observers).start()

    def get_state(self):
        return self.state

# An Observer is an object that watches another object and reacts
# whenever the Subject changes state.
class Observer(RemoteObject):
    def __init__(self, subject_name, ns_host='rocky.olin.edu'):
        
        self.name = subject_name + '_observer%d' % random.randint(0, 1000000)
        RemoteObject.__init__(self, self.name)

        Pyro.core.initClient()
        ns = Pyro.naming.NameServerLocator().getNS(ns_host)
        uri = ns.resolve(subject_name)
        self.subject = Pyro.core.getProxyForURI(uri)

        self.threadLoop()
        self.subject.register(self.uri)
    
    def notify(self):
        state = self.subject.get_state()
        print 'Notified', state

def main(script, name='bob', flag='observer', *args):
    if flag == 'observer':        
        observer = Observer(name)
        
        state = observer.subject.get_state()
        observer.subject.set_state(state+1)

        try:
            while 1: sleep(1)
        except KeyboardInterrupt:
            observer.stopLoop()
    elif flag == 'subject':
        SimpleSubject(name)


        
if __name__ == '__main__':
    main(*sys.argv)
