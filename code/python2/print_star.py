def print1(s1, s2, s3):
    print s1, s2, s3,

def print2(s1, s2, s3):
    print1(s1, s2, s3)
    print1(s1, s2, s1)
    print1(s3, s2, s1)


def print3(s1, s2, s3):
    print2(s1, s2, s3)
    print2(s1, s2, s1)
    print2(s3, s2, s1)

def printn(n, s1, s2, s3):
    if n==0:
        print s1, s2, s3,
        return
    printn(n-1, s1, s2, s3)
    printn(n-1, s2, s3, s1)
    printn(n-1, s3, s1, s2)

def print_n(s, n):
    """print the string (s) n times"""
    if n == 0:
        return
    print s
    print_n(s, n-1)

def recurse():
    recurse()

recurse()
    
printn(2, 'x', 'o', ' ')
print ''
