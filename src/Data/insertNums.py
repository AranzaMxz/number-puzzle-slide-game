from Data.conditions import checkInput

def replaceValue(values, position, newValue):
    # values == position + " " -> return a matrix with booleans (true if position + " " is on the board)
    # values[...] -> replaces with the newValue where is true
    values[values == position + " "] = newValue
    print(values)

def getPosition(values):
    # First we ask about the blank space
    while True:
        spaceEmpty = input("What space do you want to leave blank? ")
        print("you chose " + spaceEmpty)
        # Replace the value in the space selected if is accepted and free
        if checkInput(values, spaceEmpty):
            replaceValue(values, spaceEmpty, " ")
            break


    #number = int(input(f"Enter a number between 1-{len(values)**2 -1}"))

def insert(values):
    getPosition(values)
