'''
This is the Main program
'''

# Imports
from Card import *          # My Card.py
from Deck import *          # My Deck.py
from Participant import *   # My Participant.py
import Helper               # My Helper.py

# Methods
def startGameDecision():
    playerChoice = None
    while playerChoice == None:
        print("Play Blackjack? [Y]ES, [N]O: ")
        playerChoice = Helper.checkValidInput(['y', 'n'])

    if playerChoice == 'y':
        print("Let's play")     # Replace This
        table = BJTable(100.00, 8)
        table.runGame()
    else:
        print("Bye!")
        exit()

# Main Game Loop
title = "BLACKJACK".center(30,"*")
border = "*" * 30
print(title)
print(border)
while True:
    startGameDecision()