import sys, string

def process_word(word, d):
    word.lower()

    if word in d:
        d[word] += 1
    else:
        d[word] = 1
    
def process_line(line, d):
    t = line.split()

    for i in len(t):
        process_word(t[i], d)

def process_file(filename):
    d = {}
    fp = open(filename, 'r')
    for line in fp:
        process_line(line, 'd')
    return d

def print_top_ten(d):
    t = []
    for k, v in d.iteritems()
        pair = v, k
        t = t.append(pair)

    t.sort(reverse=True)
    for v, k in t[0:10]:
        print k

d = process_file('gatsby.txt')
print_top_ten(d)
