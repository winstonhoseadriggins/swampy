class ddict(dict):
    def __missing__(self, key):
        return False

def span(i, j):
    return range(i,j+1)

class Grammar:
    def __init__(self, vars, terms, start):
        """vars and terms are disjoint sets of strings;
        start is a member of terms.  rules is a mapping from
        vars to lists of strings of terms and vars.
        """
        self.vars = vars
        self.terms = terms
        self.start = start
        self.rules = dict()
    
    def add_rule(self, var, rhs):
        """add a new rule of the form '(var) can be a (rhs)'""" 
        self.rules.setdefault(var, []).append(rhs)

    def process(self, string):
        """process the given string and print 'accept' or 'reject' """
        P = ddict()
        m = 1
        for j, c in enumerate(string):
            for A, rules in self.rules.iteritems():
                for rhs in rules:
                    if rhs == c:
                        P[j,m,A] = True

        n = len(string)
        for m in span(2,n):
            for j in span(0, n-m+1):
                for k in span(1, m-1):
                    for A, rules in self.rules.iteritems():
                        for rhs in rules:
                            if len(rhs) < 2: continue
                            B, C = rhs
                            if P[j,k,B] and P[j+k,m-k,C]:
                                P[j,m,A] = True

        for var in self.vars:
            if P[0,n,var]:
                print var

def main():

    vars = set('STUAB')
    terms = set('ab')
    start = 'S'
    g = Grammar(vars, terms, start)
    g.add_rule('S', 'a')
    g.add_rule('S', 'b')
    g.add_rule('S', 'AT')
    g.add_rule('S', 'BU')
    g.add_rule('A', 'a')
    g.add_rule('B', 'b')
    g.add_rule('T', 'SA')
    g.add_rule('U', 'SB')

    g.process('ababa')

        
if __name__ == '__main__':
    main()
