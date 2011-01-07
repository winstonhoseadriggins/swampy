filename = 'background_significance_190608.tex'

for line in open(filename):
    if len(line) > 1:
        print line.strip(),
    else:
        print line
