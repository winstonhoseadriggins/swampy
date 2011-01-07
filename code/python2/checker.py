def print_n(s, n):
    """print the string n times"""
    if n <= 0:
        return
    print s,
    print_n(s, n-1)

def print_segment(s1, s2):
    """print (s1) followed by 5 copies of (s2)"""
    print s1,
    print_n(s2, 5)

def print_row(m, s1, s2):
    """print a row with (m) segments"""
    if m <= 0:
        return
    print_segment(s1, s2)
    print_row(m-1, s1, s2)

def print_rows(n, m, s1, s2):
    """print (n) rows with (m) segments"""
    if n <=0:
        return
    print_row(m, s1, s2)
    print s1
    print_rows(n-1, m, s1, s2)

def print_block(m):
    """print a block with m segments"""
    print_row(m, '+', '-')
    print '+'
    print_rows(4, m, '|', ' ')

def print_blocks(n, m):
    """print (n) blocks with (m) segments"""
    if n <=0:
        return
    print_block(m)
    print_blocks(n-1, m)

def print_board(n, m):
    """print an nxm checkerboard"""
    print_blocks(n, m)
    print_row(m, '+', '-')
    print '+'

print_board(2, 2)
