class Instrument:
    def inactive(self):
        "Inactive methods are bound to this method."
        raise NameError, 'the method you invoked is not active.'

    def _active_sweep(self):
        """This is the active version of sweep.
           It should not be invoked directly"""
        print 'sweep'

    # initially sweep is inactive
    sweep = inactive

    def activate(self, method):
        "Activate the given method."
        d = self.__class__.__dict__
        d[method] = d['_active_' + method]

    def deactivate(self, method):
        "Deactivate the given method."
        d = self.__class__.__dict__
        d[method] = d['inactive']


# create an instrument and invoke an inactive method
inst = Instrument()
try:
    inst.sweep()
except:
    print 'nope'

# activate the method and then invoke it again
inst.activate('sweep')
inst.sweep()

# deactivate the method and then invoke it again
inst.deactivate('sweep')
inst.sweep()
