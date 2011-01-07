from urllib import *

conn = urlopen('http://rocky.olin.edu/sd/code/World.py')
print conn

for line in conn.fp:
    print line,
    
