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


def sedall(pattern, sed_cmd):
    """Runs sed on each file that matches the pattern.

    pattern: glob pattern for filenames
    sed_cmd: string sed cmd to apply to each file
    """
    for filename in glob(pattern):
        if filename == 'sedall.py':
            continue

        cmd = "sed '%s' %s > temp" % (sed_cmd, filename)
        print cmd
        res, stat = pipe(cmd)

        if stat == None:
            cmd = "mv temp %s" % filename
            res, stat = pipe(cmd)

    return stat


def main(name, pattern='*.py'):
    for module in ['TurtleWorld']:
        sed_cmd = 's/^from %s/from swampy.%s/' % (module, module)
        print sed_cmd
        sedall(pattern, sed_cmd)


if __name__ == '__main__':
    stat = main(*sys.argv)
    sys.exit(stat)
