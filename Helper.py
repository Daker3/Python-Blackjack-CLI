# Helper Methods

def checkValidInput(validInputs):
    validChoice = False
    playerChoice = input().lower()
    if playerChoice not in validInputs:
        return None
    else:
        return playerChoice