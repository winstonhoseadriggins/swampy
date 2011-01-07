from sd_hw03_soln import rotate_word

def read_wordlist(filename):
    """read the given word list and return a dictionary with a
    key for each word in the file"""
    d = dict()
    for word in open(filename):
        word = word.strip().lower()
        d[word] = word
    return d

def check_rotation(word, shift, d):
    """rotate (word) by (shift).  Return the result if it is
    in (d) or None otherwise.
    """
    rot = rotate_word(word, shift)
    return d.get(rot, None)

def check_rotations(word, d):
    """rotate (word) by each shift from 1 to 13 and print
    any rotate pairs in (d)
    """
    for i in range(1,14):
        rot = check_rotation(word, i, d)
        if rot:
            print len(word), word, i, rot

def find_pairs(d):
    """print all the rotate pairs in d"""
    for word in d:
        check_rotations(word, d)

d = read_wordlist('words.txt')
find_pairs(d)

