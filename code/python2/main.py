import sys

def main(script, arg1='default1', arg2='default', *args):
    print script, arg1, arg2, args

if __name__ == '__main__':
    main(*sys.argv)
    



