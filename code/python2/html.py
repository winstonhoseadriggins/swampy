from HTMLParser import HTMLParser
from urllib import *

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print "Encountered the beginning of a %s tag" % tag

    def handle_endtag(self, tag):
        print "Encountered the end of a %s tag" % tag

p = MyHTMLParser()

conn = urlopen('http://wb/sd/index.html')
for line in conn.fp:
    p.feed(line)
