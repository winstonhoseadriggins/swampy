#!/usr/bin/env python

import sys
import sha
from xmlrpclib import *

gateway='lefthand.eecs.harvard.edu'
result = { 0 : "Success", 1 : "Capacity", 2 : "Again" }

def put(s, script, key='key', value='value', gateway=gateway, ttl=300):
    print result [s.put(Binary(sha.new(key).digest()), 
                    Binary(value), int(ttl), script)]    


def get(s, script, key='key', gateway=gateway, maxvals=10):

    placemark = Binary("")
    key = Binary(sha.new(key).digest())

    while 1:
        values, placemark = s.get(key, maxvals, placemark, script)
        for value in values: print value.data
        if (placemark.data == ""): break


if __name__ == '__main__':
    url = 'http://%s:5851/' % gateway
    s = ServerProxy(url)

    script = sys.argv[0]
    if script == 'get.py':
        get(s, *sys.argv)
    elif script == 'put.py':
        put(s, *sys.argv)
    sys.exit(0)
    



