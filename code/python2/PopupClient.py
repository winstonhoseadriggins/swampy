from RemoteObject import *

def main(script, name='bob', message='hello', *args):
    """contact the remote object with the given name and
    invoke popup with the given message"""
    ns = NameServer()
    try:
        server = ns.get_proxy(name)
    except Pyro.errors.NamingError:
        print "I can't find a remote object named " + name
        return
    print server.popup(message)

if __name__ == '__main__':
    main(*sys.argv)
