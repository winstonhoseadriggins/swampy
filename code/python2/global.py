verbose = True

def example1():
    if verbose:
        print 'Running example1'

example1()


been_called = False

def example2():
    global been_called 
    been_called = True

example2()
print been_called


count = 0

def example3():
    #global count
    count += 1

example3()
print count


known = {0:0, 1:1}

def example4():
    known[2] = 1

example4()
print known
