"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2013 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

import os
import matplotlib.pyplot as pyplot


def etime():
    """Measures user and system time this process has used.

    returns: sum of user and system time.
    """
    user, sys, chuser, chsys, real = os.times()
    return user+sys


def sum_pluseq(t, init):
    """Concatenates a list of lists into a single list using +=
    
    t: list of lists
    init: initialization for the sum

    returns: list
    """
    total = init
    for x in t:
        total += x
    return total


def sum_extend(t, init):
    """Concatenates a list of lists into a single list using list.extend

    t: list of lists
    init: initialization for the sum

    returns: list
    """
    total = init
    for x in t:
        total.extend(x)
    return total


def sum_sum(t, init):
    """Concatenates a list of lists into a single list using sum.
    
    t: list of lists
    init: initialization for the sum

    returns: list
    """
    return sum(t, init)


def test_func(f, n):
    """Tests the function, f, with a list of lists of length n.

    f: function that flattens a list of lists
    n: input size

    returns: elapsed time in seconds
    """
    t = [[1]] * n

    start = etime()
    f(t, [])
    end = etime()
    elapsed = end - start
    return elapsed


def test(name):
    """Tests the given function with a range of values for n.

    Returns: list of ns and a list of run times.
    """
    # look up the string (name) and get the function object
    f = eval(name)

    # depending on which function we are testing, we need to
    # use a different order of magnitude for (n)
    d = dict(sum_sum=1000,
             sum_pluseq=100000,
             sum_extend=100000)
    factor = d[name]

    # test (f) over a range of values for (n)
    ns = []
    ts = []
    for i in range(2, 25):
        n = factor * i
        t = test_func(f, n)
        print n, t
        ns.append(n)
        ts.append(t)

    return ns, ts


def plot(ns, ts, label, color='blue', exp=1.0):
    """Plots data and a fitted curve.

    ns: sequence of n (problem size)
    ts: sequence of t (run time)
    label: string label for the data curve
    color: string color for the data curve
    exp: exponent (slope) for the fitted curve
    """
    tfit = fit(ns, ts, exp)
    pyplot.plot(ns, tfit, color='0.7',
                linewidth=2, alpha=0.5,linestyle='dashed')
    pyplot.plot(ns, ts, label=label, color=color,
                linewidth=3, alpha=0.5)


def fit(ns, ts, exp=1.0, index=-1):
    """Fits a curve with the given exponent.

    Use the given index as a reference point, and scale all other
    points accordingly.

    ts: sequence of t (run time)
    exp: exponent (slope) for the fitted curve
    index: which point to use as a reference point
    """
    nref = ns[index]
    tref = ts[index]

    tfit = []
    for n in ns:
        ratio = float(n) / nref
        t = ratio**exp * tref
        tfit.append(t)

    return tfit


def save(root, exts=['eps', 'pdf']):
    """Saves the current figure in the given formats.

    root: string filename root
    exts: list of string extensions (specifying output formats).
    """
    for ext in exts:
        filename = '%s.%s' % (root, ext)
        print 'Writing', filename
        pyplot.savefig(filename)


def make_fig(funcs, scale='log', exp=1.0, root=''):
    """Makes a figure with the given funcs.

    funcs: list of function names
    scale: string scale for the plot: 'log' or 'linear'
    exp: expected exponent of the data
    root: string filename root (without extension)
    """
    pyplot.clf()
    pyplot.xscale(scale)
    pyplot.yscale(scale)
    pyplot.title('')
    pyplot.xlabel('n')
    pyplot.ylabel('run time (s)')

    colors = ['blue', 'orange', 'green']
    for func, color in zip(funcs, colors):
        data = test(func)
        plot(*data, label=func, color=color, exp=exp)

    pyplot.legend(loc=4)

    if root:
        save(root)
    else:
        pyplot.show()


def main(script):
    make_fig(['sum_extend', 'sum_pluseq'], exp=1.0, root='listsum1')
    make_fig(['sum_sum'], exp=2.0, root='listsum2')


if __name__ == '__main__':
    import sys
    main(*sys.argv)

