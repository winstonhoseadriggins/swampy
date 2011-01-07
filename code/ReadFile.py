import sys
import string

def process_file(filename):
    trans = string.maketrans("-'", '  ')
    
    fp = open(filename, 'r')
    for line in fp:
        line = line.translate(trans)
        for word in line.rstrip().split():
            process_word(word)

def process_word(word):
    word = word.strip(string.punctuation)
    print word

def main(name, filename='', *args):
    process_file(filename)

if __name__ == '__main__':
    main(*sys.argv)
