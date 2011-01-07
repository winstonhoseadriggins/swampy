import sys
import string
from Hist import *

class WordHist(Hist):
    def process_file(self, filename):
        fp = open(filename, 'r')
        for line in fp:
            line = line.replace('--', ' ')
            line = line.replace("'s ", ' ')
            for word in line.rstrip().split():
                self.process_word(word)

    def process_word(self, word):
        word = word.strip(string.punctuation)
        self.count(word)

            
def main(name, filename='gatsby.txt', flag=None, *args):
    whist = WordHist()
    try:
        whist.process_file(filename)
    except IOError:
        print "Can't find the file", filename

    for word, freq in whist.pdf():
        print word, freq
        
if __name__ == '__main__':
    main(*sys.argv)
