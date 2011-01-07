import string

def any_lowercase1(s):
    for c in s:
        if c in string.lowercase:
            return True
        else:
            return False

def any_lowercase2(s):
    for c in s:
        if 'c' in string.lowercase:
            return 'True'
        else:
            return 'False'

def any_lowercase3(s):
    for c in s:
        flag = c in string.lowercase
    return flag

def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or (c in string.lowercase)
    return flag

def any_lowercase5(s):
    for c in s:
        if not c in string.lowercase:
	    return False
    return True

def any_lowercase6(s):
    for c in s:
        c in string.lowercase
	if True:
	    return

print any_lowercase1('Allen')
print any_lowercase2('Allen')
print any_lowercase3('Allen')
print any_lowercase4('Allen')
print any_lowercase5('allen')
print any_lowercase6('allen')
