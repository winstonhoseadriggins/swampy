import urllib

zipcode = '02492'

url = 'http://uszip.com/zip/' + zipcode
conn = urllib.urlopen(url)

for line in conn.fp:
    line = line.strip()
    if 'Needham' in line: print line
    if 'Population' in line: print line
    if 'Longitude' in line: print line
