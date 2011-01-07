import string

def id_genfun():
    for c in string.uppercase:
        yield c

idgenerator = id_genfun()

print idgenerator
print type(idgenerator)
print idgenerator.next()

for id in idgenerator:
    print id
