#!/usr/bin/python

"""
Copyright 2012 Allen B. Downey
Distributed under the GNU General Public License at gnu.org/licenses/gpl.html.
"""

import os, sys
from glob import glob

def pipe(cmd):
    """Runs a command in another process and returns the result.

    cmd: string shell command
    """
    fp = os.popen(cmd)
    res = fp.read()
    stat = fp.close()
    return res, stat


def sedall(pattern='*.py', sed_cmd='s/^from World/from swampy.World/'):
    """Runs sed on each file that matches the pattern.

    pattern: glob pattern for filenames
    sed_cmd: string sed cmd to apply to each file
    """
    for file in glob(pattern):
        print file
        cmd = "sed '%s' %s > temp" % (sed_cmd, file)
        print cmd
        res, stat = pipe(cmd)

        if stat == None:
            cmd = "mv temp %s" % file
            res, stat = pipe(cmd)

    return stat


def main(name, pattern='*.tex', sed_cmd='s/Spring 2004/Fall 2004/'):
    sedall(pattern, sed_cmd)


if __name__ == '__main__':
    stat = main(*sys.argv)
    sys.exit(stat)
