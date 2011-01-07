import sys

def main(name, filename):
    fp = open(filename, 'r')
    for line in fp:
        print line

if __name__ == '__main__':
    try:
        main(*sys.argv)
    except TypeError:
        print 'Wrong number of arguments.\nUsage:'
        print 'python', sys.argv[0], 'filename'

