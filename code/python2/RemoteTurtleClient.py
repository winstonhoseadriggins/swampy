from RemoteObject import *

code = """
def square(t):
    for i in range(4):
        t.fd(100)
        t.lt()
bob = Turtle()
square(bob)
"""

def main(script, name='bob', *args):
    ns = NameServer()
    server = ns.get_proxy(name)
    server.run_message(code)

if __name__ == '__main__':
    main(*sys.argv)
