import sys
import shelve
from imdb import process_file
import anydbm

films = shelve.open('filmography.db', 'c')
actor = ''
t = []

def store_info(new_actor, date, title, role):
    global actor, t

    if new_actor != actor:
        if actor:
            films[actor] = t
        actor = new_actor
        t = []

    t.append(title + date)


def read_db():
    print 'Reading...'
    for key in films:
        print key


def main(script, command=None, *args):
    if command == 'actors':
        process_file('actors.list.gz', store_info)
    elif command == 'actresses':
        process_file('actresses.list.gz', store_info)
    elif command == 'read':
        read_db()
    elif command == 'stats':
        print len(films)
    else:
        print 'Usage: ' + script + ' actors | actresses | read'

    films.close()

if __name__ == '__main__':
    main(*sys.argv)

