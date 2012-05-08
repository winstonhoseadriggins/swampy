"""

Solution to the second batch of Car Talk Puzzlers
Think Python
Allen B. Downey

"""

def make_word_list3():
    """read the words in words.txt and return a dictionary
    that contains the words as keys"""
    d = dict()
    fin = open('words.txt')
    for line in fin:
        word = line.strip().lower()
        d[word] = word

    # have to add single letter words to the word list;
    # also, the empty string is considered a word.
    for letter in ['a', 'i', '']:
        d[letter] = letter
    return d

wordlist = make_word_list3()

def check_word(word):
    """check to see if the word has the following property:
    removing the first letter yields a word in (d),
    and removing the second letter yields a word in (d)."""
    return word[1:] in wordlist and word[0] + word[2:] in wordlist

def check_all_words():
    for word in wordlist:
        if check_word(word):
            print word, word[1:], word[0] + word[2:]

#d = make_word_list3()
#check_all_words(wordlist)

"""a string is reducible if it is in the dictionary and
has at least one child that is reducible.  The empty string
is also reducible."""

"""memo is a dictionary that maps from each word that is known
to be reducible to each of its reducible children."""
memo = dict()

def children(word):
    """build and return a list of all words that can be formed
    by removing one letter from (word)"""
    res = []
    for i in range(len(word)):
        child = word[:i] + word[i+1:]
        if child in wordlist:
            res.append(child)
    return res

def reduce(word):
    """if this word is reducible, return a list of its reducible
    children; also add an entry to the memo dictionary."""

    # the empty string is reducible
    if word == '':
        return [word]
    
     # if have already checked this word, return the answer
    if word in memo:
        return memo[word]

    # check each of the children and make a list of the reducible ones
    res = []
    for child in children(word):
        t = reduce(child)
        if t:
            res.append(child)

    # memoize and return the result
    memo[word] = res
    return res

def reduce_all_words(flag=False):
    """check all the words in the wordlist.
    if flag==True, print the reducible words and their lengths.
    """
    for word in wordlist:
        t = reduce(word)
        if t and flag:
            print len(word), word

def print_trail(word):
    """print the sequence of words that reduces this word to the
    empty string; if there is more than one choice, it chooses the
    first."""
    if len(word) == 0:
        return
    print word,
    t = reduce(word)
    print_trail(t[0])


reduce_all_words(True)

reduce('complecting')
print_trail('complecting')

