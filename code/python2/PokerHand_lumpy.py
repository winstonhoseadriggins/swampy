import sys
import Lumpy
from Card import *

class PokerHand(Hand):
    def suit_hist(self):
        """build a histogram of the suits that appear in the hand"""
        self.suits = {}
	for card in self.cards:
	    self.suits[card.suit] = self.suits.get(card.suit, 0) + 1

    def has_flush(self):
        """if the hand has a flush, set the label and return True
        otherwise return False"""
        self.suit_hist()
        for val in self.suits.values():
            if val >= 5:
                return True
	return False


def main(*args):

    # initialize Lumpy
    lumpy = Lumpy.Lumpy()
    lumpy.make_reference()

    # make a deck
    deck = Deck()
    deck.shuffle()

    # deal the cards and classify the hands
    for i in range(6):
        hand = PokerHand()
        deck.move_cards(hand, 7)
        print hand
        print hand.has_flush()
        print ''

    # generate UML diagrams
    lumpy.object_diagram()
    lumpy.class_diagram()


if __name__ == '__main__':
    main(*sys.argv)

