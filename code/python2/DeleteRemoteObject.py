from RemoteObject import *
import sys

ns = NameServer()
t = ns.clear(*sys.argv[1:])


