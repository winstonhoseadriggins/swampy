"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

import os


def print_diagram(lumpy, filename):
    if lumpy.od:
        lumpy.od.printfile(filename)
    else:
        lumpy.cd.printfile(filename)

    cmd = 'epstopdf %s' % filename
    fp = os.popen(cmd)
    res = fp.read()
    stat = fp.close()
    return res, stat
