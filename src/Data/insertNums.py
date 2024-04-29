from Data.conditions import checkInput
from Data.conditions import checkNotNumber
from Board.matrix import printBoard

def replaceValue(values, position, newValue):
    # values == position + " " -> return a matrix with booleans (true if position + " " is on the board)
    # values[...] -> replaces with the newValue where is true
    values[values == position + " "] = newValue
    #print(values)

def getPosition(values):
    # First we ask about the blank space
    while True:
        spaceEmpty = input("What space do you want to leave blank? ")
        # Replace the value in the space selected if is accepted and free
        if checkInput(values, spaceEmpty):
            replaceValue(values, spaceEmpty, "  ")
            printBoard(len(values), values)
            break
    for i in range(len(values)**2 - 1):
        while True:
            selection = input(f"\nWhere do you wanna put the {i + 1} ?: ")
            if checkInput(values, selection) and checkNotNumber(selection):
                num = str(i + 1 ) + " "
                replaceValue(values, selection, num)
                printBoard(len(values), values)
                break

def insert(values):
    getPosition(values)
