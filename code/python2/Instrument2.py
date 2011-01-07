class Instrument(object):

    def __new__(cls, address, *args, **kwds):
        d = cls._get_instruments()
        if address in d:
            d[address].__class__ = cls
        else:
            d[address] = object.__new__(cls, *args, **kwds)
        return d[address]

    def __init__(self, address):
        self.address = address
        self.configure()

    def reconfigure(self, cls, *args, **kwds):
        self.__class__ = cls
        self.configure(*args, **kwds)

    # put general-purpose code for talking to the instrument here
    
class HP40c(Instrument):
    _instruments = {}
    def _get_instruments(cls): return HP40c._instruments
    _get_instruments = classmethod(_get_instruments)

class HP40cRaw(HP40c):
    def configure(self):
        print 'configure as RawHP40c'

class HP40cVoltageSource(HP40c):
    def configure(self):
        print 'configure as VoltageSource'

    def sweep(self):
        print 'sweep_voltage'

class HP40cCurrentSource(HP40c):
    def configure(self):
        print 'configure as CurrentSource'

    def sweep(self):
        print 'sweep_current'


inst = HP40cRaw(883)
try:
    inst.sweep()
except:
    print 'nope'

inst.reconfigure(HP40cVoltageSource)
inst.sweep()

inst.reconfigure(HP40cCurrentSource)
inst.sweep()

inst2 = HP40cVoltageSource(883)
inst2.sweep()

print inst is inst2

inst3 = HP40cCurrentSource(885)
inst3.sweep()

print inst is inst3


class Agilent34980A(Instrument):
    _instruments = {}
    def _get_instruments(cls): return Agilent34980A._instruments
    _get_instruments = classmethod(_get_instruments)

class Agilent34980ARaw(Agilent34980A):
    def configure(self):
        print 'configure as RawAgilent34980A'

class Agilent34980AVoltageSource(Agilent34980A):
    def configure(self):
        print 'configure as VoltageSource'

    def sweep(self):
        print 'sweep_voltage'

class Agilent34980ACurrentSource(Agilent34980A):
    def configure(self):
        print 'configure as CurrentSource'

    def sweep(self):
        print 'sweep_current'


inst = Agilent34980ARaw(883)
try:
    inst.sweep()
except:
    print 'nope'

inst.reconfigure(Agilent34980AVoltageSource)
inst.sweep()

inst.reconfigure(Agilent34980ACurrentSource)
inst.sweep()

inst2 = Agilent34980AVoltageSource(883)
inst2.sweep()

print inst is inst2

inst3 = Agilent34980ACurrentSource(885)
inst3.sweep()

print inst is inst3


print HP40c._instruments
print Agilent34980A._instruments
