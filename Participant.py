'''
Classes for the participants
'''

# Imports
from Card import *  # My Card.py
from Deck import *  # My Deck.py
import Helper       # My Helper.py

'''
Class Participant
'''
class Participant():
    
    # Constructor

    '''
    Constructor: Default

    Initially empty hand and hasn't busted
    '''
    def __init__(self):
        self._currentHand = Hand(0)
        self._hands = [self._currentHand]
        self._handCount = 0
        self._currentHandIndex = 0

    # Methods
    def getHand(self):
        return self._currentHand

    '''
    Method: newHand(wager)

    Adds a new hand
    Passes wager to new Hand.
    '''
    def newHand(self, wager):
        hand = Hand(wager)
        self._hands.append(hand)
    
    '''
    Method: hit(card)

    Draw another Card from the Shoe.
    '''
    def hit(self, card):
        self._hands[self._currentHandIndex].addCard(card)

    '''
    Method: stand()
    '''
    def stand(self):
        self._hands[self._currentHandIndex].stand()

''''
Class: Dealer
'''
class Dealer(Participant):
    
    # Constructor
    def __init__(self):
        super().__init__()
        self._holeRevealed = False

    '''
    Method: __str__()

    String output
    '''
    def __str__(self):
        dealerString = "Dealer: "
        i = 0
        for card in self._currentHand.getCards():
            dealerString += " "
            if i == 0 and self._holeRevealed == False:    # Think of a way without i var
                dealerString += "??"
            else:
                dealerString += str(card)
            i += 1
        return dealerString

    '''
    Method: revealHole()
    
    Marks the Hole card so it can be shown.
    '''
    def revealHole(self):
        self._holeRevealed = True

'''
Class: Player
'''
class Player(Participant):

    # Constructor
    def __init__(self, credits):
        super().__init__()
        self.credits = credits

    # Methods
    '''
    Method: __str__()

    String output
    '''
    def __str__(self):
        playerString = "Player: "
        for card in self._currentHand.getCards():
            playerString += " "
            playerString += str(card)
        return playerString


    '''
    Method: doubleDown(card)

    Double wager and get one more card
    '''
    def doubleDown(self, card):
        self._hands[self._currentHandIndex].addCard(card)

    '''
    Method: split(card, card)

    Split hand
    '''

'''
Class: BJTable

Table represents the game. It contains a shoe, Dealer, and Player.
'''
class BJTable():

    # Constructor
    def __init__(self, credits, decks):
        self.dealer = Dealer()
        self.player = Player(credits)
        self.shoe = Shoe(decks)

    # Methods
    
    '''
    Method runGame()

    Round Loop
    '''
    def runGame(self):
        # Initial Hands
        self.player.newHand(0)              # Implement wager amount
        self.dealer.newHand(0)
        self.player.hit(self.shoe.draw())
        self.dealer.hit(self.shoe.draw())
        self.player.hit(self.shoe.draw())
        self.dealer.hit(self.shoe.draw())
        self.dealer.getHand().setInitial()
        self.player.getHand().setInitial()
        print(self.dealer)
        print(self.player)

        # Player Loop
        currentHand = self.player.getHand()
        stillPlaying = currentHand.softTotal() < 21 and currentHand.isStanding() == False
        while stillPlaying == True:
            self.playerDecision()
            stillPlaying = currentHand.softTotal() < 21 and currentHand.isStanding() == False
        if self.player.getHand().isBusted():
            print("You busted!")

        # Dealer Loop
        self.dealer.revealHole()
        print("\nDealer's Turn")
        print(self.dealer)
        dealerCurrentHand = self.dealer.getHand()
        dealerStillPlaying = dealerCurrentHand.softTotal() < 18 and dealerCurrentHand.isStanding() == False
        while dealerStillPlaying:
            self.dealer.hit(self.shoe.draw())
            print(self.dealer)
            dealerStillPlaying = dealerCurrentHand.softTotal() < 18 and dealerCurrentHand.isStanding() == False

        # Results
        print("\nFinal Hands")
        print(self.dealer)
        print(self.player)
        if dealerCurrentHand.softTotal() < currentHand.softTotal():
            print("Player Won! $AMOUNT")        # Implement prize amount
        elif dealerCurrentHand.softTotal() > currentHand.softTotal() or currentHand.isBusted:
            print("Player Lost!")
        else:
            print("Push. Bets returned.")

    '''
    Method: playerDecision()

    Wait for player input for hand decision.
    '''
    def playerDecision(self):
        validInputs = []
        validChoices = ""
        tempHand = self.player.getHand()
        if tempHand.isInitial():
            if tempHand.softTotal() < 21:
                validInputs.append('h')
                validChoices += "[H]IT"
            validInputs.append('s')
            validChoices += ", [S]TAND"
            validInputs.append('d')
            validChoices += ", [D]OUBLE DOWN"
            if tempHand.isPair():
                validInputs.append('p')
                validChoices += ", S[P]LIT"

        playerChoice = None

        while playerChoice == None:
            print(validChoices)
            playerChoice = Helper.checkValidInput(validInputs)
            
        if playerChoice == 'h':
            self.player.hit(self.shoe.draw())
            print(self.dealer)
            print(self.player)
        elif playerChoice == 's':
            self.player.stand()
            return True
        elif playerChoice == 'd':
            print("DOUBLE DOWN")            # Implement Later
        elif playerChoice == 'p':
            print("SPLIT")                  # Implement Later