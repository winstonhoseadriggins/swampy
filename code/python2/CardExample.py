#!/usr/bin/python

import sys
from random import randint

class Card:
    suitList = ["Clubs", "Diamonds", "Hearts", "Spades"]
    rankList = ["narf", "Ace", "2", "3", "4", "5", "6", "7", 
              "8", "9", "10", "Jack", "Queen", "King"]

    def __init__(self, suit=0, rank=0):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return '%s of %s' % (Card.rankList[self.rank],
                             Card.suitList[self.suit])

    def __cmp__(self, other):
        return self.suit - other.suit or cmp_rank(self.rank, other.rank)

def cmp_rank(r1, r2):
    if r1==1: r1=13
    if r2==1: r2=13
    return r1-r2
    

class Deck:
    # if you don't provide a deck, the initializer creates
    # a new deck and 52 cards.  If you do provide a deck,
    # the initializer makes a copy that refers to the same
    # set of cards as the original.  start and stop let you
    # copy part of a deck.
    def __init__(self, deck=None, start=0, stop=None):
        if deck == None:
            self.full_deck()
        else:
            if stop == None:
                self.cards = deck.cards[start:]
            else:
                self.cards = deck.cards[start:stop]

    # create a complete deck of cards
    def full_deck(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                self.cards.append(Card(suit, rank))

    # print a deck
    def __str__(self):
        res = ''
        for card in self.cards:
            res += str(card) + '\n'
        return res

    # add a card to the deck
    def add_card(self, card):
        self.cards.append(card)

    # remove and return a card from the deck.  by default, pop
    # the last card
    def pop_card(self, i=-1):
        return self.cards.pop(i)


    # move the given number of cards from the deck into the Hand
    def deal(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())

    # shuffle the deck
    def shuffle(self):
        n = len(self.cards)
        for i in range(n):
            j = randint(i, n-1)
            swap_items(self.cards, i, j)

# swap two items in a mutable sequence
def swap_items(seq, i, j):
    seq[i], seq[j] = seq[j], seq[i]


# a Hand is a kind of Deck
class Hand(Deck):
    def __init__(self, label=''):
        self.label = label
        self.cards = []


class PokerHand(Hand):
    
    # build a histogram of the suits that appear in the hand,
    # but only if it doesn't exist yet
    def suit_hist(self):
        if hasattr(self,'suits'): return
        self.suits = {}
	for card in self.cards:
	    self.suits[card.suit] = self.suits.get(card.suit, 0) + 1

    # if the hand has a flush, return 1; otherwise return 0
    def has_flush(self):
        self.suit_hist()
        for val in self.suits.values():
            if val >= 5:
                return 1
	return 0


def main(*args):
    deck = Deck()
    deck.shuffle()

    # deal three hands of 5 cards, and check for flushes
    for i in range(3):
        hand = PokerHand()
        deck.deal(hand, 5)
        if hand.has_flush():
            self.label = 'flush'
        print hand.label
        print hand
    
    
if __name__ == '__main__':
    main(*sys.argv)
