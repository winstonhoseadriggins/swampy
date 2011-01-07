
def is_palindrome(word):
    """return True if the given word is a palindrome;
    otherwise return False"""
    if len(word) < 2: return True
    if word[0] != word[-1]: return False
    middle = word[1:-1]
    return is_palindrome(middle)

def is_palindrome2(word):
    """return True if the given word is a palindrome;
    otherwise return False"""
    t1 = list(word)
    t2 = list(word)
    t2.reverse()
    return t1 == t2

def is_palindrome(word):
    i = 0
    j = len(word)-1

    while i<j:
        if word[i] != word[j]:
            return False
        i = i+1
        j = j-1

    return True


def has_e(word):
    """return True if the word has an e"""
    return 'e' in word

def has_no_e(word):
    """return True if the word has no e"""
    return 'e' not in word

def avoids(word, forbidden):
    """return True if none of the forbidden letters appears in the word"""
    for c in word:
        if c in forbidden:
            return False
    return True

def uses_all(word, required):
    """return True if all the required letters appear in the word"""
    for c in required: 
        if c not in word:
            return False
    return True

def uses_only(word, available):
    """return True if the word only contains available letters"""
    for c in word: 
        if c not in available:
            return False
    return True

def is_tautonym(word):
    """return True if the word is a tautonym, like beriberi and tomtom"""
    if len(word)%2: return
    i = len(word)/2
    return word[:i] == word[i:]

def is_abecedarian(word):
    """return True if the letters of the word are in alphabetical order"""
    for i in range(len(word)-1):
        if word[i+1] <= word[i]:      # strict version: no doubles
            return False
    return True

def is_abecedarian(word):
    i = 0
    while i < len(word)-1:
        if word[i+1] < word[i]:
            return False
        i = i+1
    return True


def rotate_word(word, shift=1):
    """rotate the letters of a word by the given shift amount"""
    res = ''
    for c in word:
        res += rotate_letter(c, shift)
    return res

def rotate_letter(c, shift=1):
    """rotate a letter by the given shift amount"""
    if c in string.lowercase:
        return rotate(c, shift, 'a')
    elif c in string.uppercase:
        return rotate(c, shift, 'A')
    else:
        return c

def rotate(c, shift, base):
    """rotate a letter by the given shift amount,
    relative to the given base"""
    x = ord(c) - ord(base)
    y = (x + shift) % 26 + ord(base)
    return chr(y)

def apply_filter(file, filter, *args):
    """read each line of the given file and apply the given filter.
    If the result is True, print the line."""
    try:
        fp = open(file, 'r')
    except IOError:
        print "Couldn't find a file named", file
        sys.exit()

    for word in fp:
        word = string.rstrip(word)
        word = string.lower(word)
        if filter(word, *args):
            print word

fin = file('words.txt')
for line in fin:
    word = line.strip()
    if is_palindrome(word):
        print word


