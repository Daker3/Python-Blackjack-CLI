'''
Classes used to represent a Card
'''

# Imports
from enum import Enum


'''
Class: Rank

Rank represents card values Ace through King.
'''
class Rank(Enum):

    # Static Variables
    ACE = "A"
    TWO = "2"
    THREE = "3"
    FOUR = "4"
    FIVE = "5"
    SIX = "6"
    SEVEN = "7"
    EIGHT = "8"
    NINE = "9"
    TEN = "10"
    JACK = "J"
    QUEEN = "Q"
    KING = "K"

    # Methods
    def __str__(self):
        return self.value

    def getValue(self):
        if self in [Rank.TEN, Rank.JACK, Rank.QUEEN, Rank.KING]:
            return 10
        elif self == Rank.ACE:
            return 1
        else:
            return int(self.value)
        
    def isFace(self):
        if self in [Rank.JACK, Rank.QUEEN, Rank.KING]:
            return True
        else:
            return False


'''
Class: Suit

Suit represents Heart, Spade, Diamond, and Club.
'''
class Suit(Enum):

    # Static Variables
    HEART = "♥️"
    SPADE = "♠️"
    DIAMOND = "♦️"
    CLUB = "♣️"

    # Methods
    def __str__(self):
        return self.value

'''
Class: Card

A Card has a Rank and Suit.
'''
class Card():

    # Constructor
    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit

    # Methods
    def __str__(self):
        return f"{self._rank}{self._suit}"
    
    def getValue(self):
        return self._rank.getValue()

    def getRank(self):
        return self._rank

    def getSuit(self):
        return self._suit
    
    def isFace(self):
        return self._rank.isFace()

'''
Class: Hand

A Hand will contain 2 or more Cards.
'''
class Hand():

    # Constructor
    def __init__(self, wager):
        self._cards = []
        self._busted = False
        self._standing = False
        self._wager = wager
        self._initialHand = False
    # Methods
    '''
    Method: printHand()

    Outputs the current hand and total.
    '''
    def printHand(self):
        for card in self._cards:
            print(card)

    def getCards(self):
        return self._cards

    def isBusted(self):
        return self._busted

    def stand(self):
        self._standing = True
    
    def isStanding(self):
        return self._standing

    '''
    Method: total();

    Returns the hard total value of the hand.
    '''
    def hardTotal(self):
        total = 0
        aceCount = 0
        for card in self._cards:
            if card.getRank() == Rank.ACE:
                aceCount += 1
            else:
                total += card.getValue()

        # Calculate Aces
        total += aceCount

        if total > 21:
            self._busted = True
        elif total == 21:
            self.stand
        return total
    
    '''
    Method: soft()
    '''
    def softTotal(self):
        total = 0
        aceCount = 0
        for card in self._cards:
            if card.getRank() == Rank.ACE:
                aceCount += 1
            else:
                total += card.getValue()

        # Calculate Aces
        total += aceCount
        if total < 12 and aceCount > 0:
            total += 10

        if total > 21:
            self._busted = True
        elif total == 21:
            self.stand
        return total

    '''
    Method: addCard(card)

    Adds a card to the hand
    '''
    def addCard(self, card):
        self._cards.append(card)

    '''
    Method: split()

    Pops one of the cards and draws another
    '''
    def split(self, card1, card2):
        '''
        todo: exception if:
            cards are not same rank
            more than two cards
                Although, may push that to game loop to check
        '''
        return self._cards.pop()

    '''
    Method: discardHand()

    Clears the Hand.
    '''
    def discardHand(self):
        self._cards.clear()

    '''
    Method: setInitial()

    Marks the hand as initialized (first 2 cards).
    '''
    def setInitial(self):
        self._initialHand = True
    def isInitial(self):
        return self._initialHand
    
    '''
    Method: isPair

    Checks if the hand is a Pair.
    '''
    def isPair(self):
        if self._initialHand:
            if self._cards[0].getRank() == self._cards[1].getRank():
                return True
        else:
            return False