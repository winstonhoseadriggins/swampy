#!/usr/bin/python

"""This file contains code for use with "Think Bayes",
by Allen B. Downey, available from greenteapress.com

Copyright 2013 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html


Setup:

1) Go to redistogo.com and create a free Nano database.

   Note the host, port and authcode.  

   Add the host and port info to the Model object
   below.  In general you don't want to put authcodes in your
   programs (unless you want to make the database globally accessible).

   Instead, add a line like this to your .bashrc file:

export REDIS_AUTH="374238957839837549872349577"

   To re-run the .bashrc file, run this at the linux prompt

$ . ~/.bashrc

2) Install the python-redis package

sudo apt-get install python-redis

3) Run this program

python bad_game.py
"""

import os
import redis
import sys

class Model(object):
    """Provides access to a Redis instance on Redis To Go"""

    host = 'dory.redistogo.com'
    port = 10534

    def __init__(self):
        try:
            password = os.environ['REDIS_AUTH']
        except KeyError:
            print 'Environment variable REDIS_AUTH is not set.'
            sys.exit()
        
        self.r = redis.StrictRedis(host=self.host, 
                                   port=self.port,
                                   password=password,
                                   db=0)

    def key(self, game_id):
        """Makes a key for a given game ID.

        game_id: str
        returns: string key
        """
        return 'bad_game_%s' % game_id

    def new_game(self):
        """Creates a new game.

        returns: str game ID
        """
        # add a new game to the set
        game_id = self.r.hincrby('bad_game', 'game_counter', 1)
        self.r.sadd('bad_game_gameset', game_id)

        # initialize game state
        self.set_game_state(game_id, 'waiting')
        return game_id

    def get_games(self):
        """Returns a set of game IDs.

        returns: set of str
        """
        return self.r.smembers('bad_game_gameset')
    
    def remove_game(self, game_id):
        """Removes a game.

        game_id: str
        """
        # remove game state
        self.remove_game_state(game_id)
        # remove game id
        return self.r.srem('bad_game_gameset', game_id)

    def remove_all_games(self):
        """Removes all games.
        """
        for game_id in self.get_games():
            self.remove_game(game_id)

    def set_game_state(self, game_id, value):
        """Initializes game state.

        game_id: str
        value: game state
        """
        key = self.key(game_id)
        self.r.hset(key, 'state', value)

    def get_game_state(self, game_id):
        """Gets game state.

        game_id: str
        """
        key = self.key(game_id)
        return self.r.hget(key, 'state')
        
    def remove_game_state(self, game_id):
        """Removes game state.

        game_id: str
        """
        key = self.key(game_id)
        return self.r.hdel(key, 'state')
        

class Controller(object):

    def __init__(self, model):
        """Initializes the controller.

        model: Model object
        """
        self.model = model
    
    def new_game(self):
        """Creates a new game.

        returns: str game ID
        """
        return self.model.new_game()

    def play_game(self, game_id):
        """Plays a game.

        game_id: str game id
        """
        state = self.model.get_game_state(game_id)
        print "Don't press Enter!"
        raw_input()
        self.lose_game(game_id)

    def lose_game(self, game_id):
        """Indicates that this player lost.

        game_id: str game id        
        """
        login = os.getlogin()
        state = '%s lost' % login
        self.model.set_game_state(game_id, state)
        

class TextView(object):
    """A text based view of the model."""

    def __init__(self, model):
        """Initializes the view."""
        self.model = model
    
    def display_games(self):
        """Prints the games and their state."""
        for game_id in self.model.get_games():
            print game_id, self.model.get_game_state(game_id)
    

def main(script):
    model = Model()
    view = TextView(model)
    controller = Controller(model)

    # clear the database
    #model.remove_all_games()

    print 'Adding new game'
    game_id = controller.new_game()

    print 'Games'
    view.print_games()

    print 'Playing game', game_id
    controller.play_game(game_id)

    print 'Games'
    view.print_games()


if __name__ == '__main__':
    main(*sys.argv)
