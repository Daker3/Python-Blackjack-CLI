'''
Classes used for Decks
'''

# Imports
from Card import *  # My Card.py
import random

'''
Class: Deck

A Deck represents a complete set of Cards (i.e. all Ranks and Suits).
'''
class Deck():

    # Constructor

    '''
    Constructor: Default

    Builds a List representing a 52 card deck.
    '''
    def __init__(self):
        self._cards = []
        for suit in Suit:
            for rank in Rank:
                self._cards.append(Card(rank, suit))
                # print(f"{deck[-1]}")          # Debug. -1 is last item in List

    # Methods

    '''
    Method: size()

    Should always be 52, but writing this more generally.
    '''
    def size(self):
        return len(self._cards)

    '''
    Method: getCards()

    Returns the List of cards
    '''
    def getCards(self):
        return self._cards

    '''
    Method: print()

    Prints each card in the deck.
    '''
    def print(self):
        for card in self._cards:
            print(f"{card}")

'''
Class: Shoe

A Shoe represents multiple Decks.
'''
class Shoe():

    # Constructor
    
    '''
    Constructor: Default

    Builds a list of Decks. 8 is the default.

    decks = initial decks
    shoe = shuffled cards
    '''
    def __init__(self, size=8):
        self._cards = []
        self._drawn = []
        for i in range(size):
            deck = Deck()
            for card in deck.getCards():
                self._cards.append(card)
        self.shuffle()

    # Methods

    '''
    Method: shuffle()

    Takes the List of Cards and shuffles it.
    If there were any Cards drawn, reinsert them.
    '''
    def shuffle(self):
        for card in self._drawn:
            self._cards.append(self._drawn.pop)
        random.shuffle(self._cards)

    '''
    Method: draw()

    Removes a Card from the List of Cards, returns it, and logs it into the Drawn List.
    '''
    def draw(self):
        drawnCard = self._cards.pop()
        self._drawn.append(drawnCard)
        return drawnCard