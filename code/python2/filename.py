def split_email(addr):
    t = addr.split('@')
    if len(t) == 2:
        return t
    else:
        raise ValueError, 'not a valid email address'


addr = 'monty@python.org'
uname, domain = split_email(addr)
print uname
print domain
