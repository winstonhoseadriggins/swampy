#!/usr/bin/python
import os, sys
from glob import glob
from optparse import OptionParser

def pipe(cmd):
    fp = os.popen(cmd)
    res = fp.read()
    stat = fp.close()
    return res, stat

def main(name, *argv):
    parser = OptionParser()
    parser.add_option("-f", "--filter", dest="filter")
    (options, files) = parser.parse_args()

    filter = options.filter
    print filter
    print files
    
    for file in files:
        print file
        cmd = "%s %s > temp" % (filter, file)
        res, stat = pipe(cmd)
        print res, stat
        
        if not stat:
            cmd = "mv temp %s" % file
            res, stat = pipe(cmd)

    return stat

if __name__ == '__main__':
    stat = main(*sys.argv)
    sys.exit(stat)
