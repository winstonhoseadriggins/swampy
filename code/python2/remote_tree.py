from RemoteObject import *

ns = NameServer()
world = ns.get_proxy('allen')

code = open('tree.py').read()
print code
world.run_message(code)
