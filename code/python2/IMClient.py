from RemoteObject import *

def main(script, name='bob', message='hello', *args):
    try:
        server = get_remote_object(name)
    except Pyro.errors.NamingError:
        print "I can't find a remote object named " + name
        return
    print server.popup(message)

if __name__ == '__main__':
    main(*sys.argv)
