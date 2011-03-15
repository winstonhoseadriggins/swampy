"""This module is part of Swampy, a suite of programs available from
allendowney.com/swampy.

Copyright 2010 Allen B. Downey
Distributed under the GNU General Public License at gnu.org/licenses/gpl.html.
"""

import unittest

import remote_object

class Tests(unittest.TestCase):

    def test_remote_object(self):
        name = 'remote_object'
        group = 'test'

        # find the name server
        ns = remote_object.NameServer()

        # if it doesn't have a group named test, make one
        if ns.query(group) == 0:
            ns.delete_group(group)
            
        print 'Making group %s...' % group
        ns.create_group(group)

        # create a remote object and connect it
        full_name = '%s.%s' % (group, name)
        server = remote_object.RemoteObject(full_name, ns)

        # confirm that the group and object are on the name server
        self.assertEquals(ns.query(group), 0)
        self.assertEquals(ns.query(name, group), 1)   
        
        t = ns.get_remote_object_list(group=group)
        self.assertTrue(name in t)

        # create a Watcher and then run the server loop in a thread
        try:
            watcher = remote_object.Watcher(server.cleanup)
        except SystemExit:
            print 'Watcher exited.'

        child = remote_object.MyThread(client_code, full_name, server)
        server.stoppableLoop()
        print 'Server done.'

        ns.delete_group(group)

        # confirm that the group and object are gone
        self.assertEquals(ns.query(group), -1)


def client_code(full_name, server):
    # get a proxy for this object
    # and invoke a method on it
    ns = remote_object.NameServer()
    proxy = ns.get_proxy(full_name)
    print proxy

    # stop the server
    server.stopLoop()
    server.join()

    # child thread completes
    print 'Thread complete.'



if __name__ == '__main__':
    unittest.main()
