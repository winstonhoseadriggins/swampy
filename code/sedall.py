#!/usr/bin/python
import os, sys
from glob import glob

def pipe(cmd):
    fp = os.popen(cmd)
    res = fp.read()
    stat = fp.close()
    return res, stat

def main(name, files='*.tex', sed_cmd='s/Spring 2004/Fall 2004/'):
    for file in glob(files):
        print file
        cmd = "sed '%s' %s > temp" % (sed_cmd, file)
        print cmd
        res, stat = pipe(cmd)

        if stat == None:
            cmd = "mv temp %s" % file
            res, stat = pipe(cmd)

    return stat

if __name__ == '__main__':
    stat = main(*sys.argv)
    sys.exit(stat)
