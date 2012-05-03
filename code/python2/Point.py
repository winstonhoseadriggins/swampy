"""

Code example from Think Python, by Allen B. Downey.
Available from http://thinkpython.com

Copyright 2012 Allen B. Downey.
Distributed under the GNU General Public License at gnu.org/licenses/gpl.html.

"""

class Point:
    """Represents a point in 2-D space."""

def print_point(p):
    print '(%g, %g)' % (p.x, p.y)


def main():
    blank = Point()
    blank.x = 3
    blank.y = 4
    print_point(blank)


if __name__ == '__main__':
    main()

