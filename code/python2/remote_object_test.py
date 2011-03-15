"""Test code for remote_object.py

Copyright 2010 Allen B. Downey
Distributed under the GNU General Public License at gnu.org/licenses/gpl.html.
"""

import sys

import remote_object

def main(script, name='remote_object', group='test', *args):

    # find the name server
    ns = remote_object.NameServer()

    # if the group already exists, delete it
    if ns.query(group) == 0:
        print 'Deleting group %s...' % group
        ns.delete_group(group)

    # make the group
    print 'Creating group %s...' % group
    ns.create_group(group)

    # create a remote object and connect it
    full_name = '%s.%s' % (group, name)
    server = remote_object.RemoteObject(full_name, ns)

    # confirm that the group and object are on the name server
    print group, ns.query(group)
    print full_name, ns.query(name, group)    
    print group, ns.get_remote_object_list(group=group)

    # create a Watcher and then run the server loop in a thread
    watcher = remote_object.Watcher(server.cleanup)

    # here's what the child thread runs
    def client_code(full_name, server):
        # get a proxy for this object
        # and invoke a method on it
        ns = remote_object.NameServer()
        proxy = ns.get_proxy(full_name)
        
        # invoke one of its methods remotely
        print proxy.__hash__()

        # stop the server
        server.stopLoop()
        server.join()

        # child thread completes
        print 'Thread complete.'

    child = remote_object.MyThread(client_code, full_name, server)

    # here's what the parent thread runs
    server.stoppableLoop()
    print 'Server done.'

    print 'Deleting group %s...' % group
    ns.delete_group(group)

if __name__ == '__main__':
    main(*sys.argv)
