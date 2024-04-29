import numpy as np

def checkInput(values, position):
    # The input is in the matrix 
    if np.any(values == position + " "):
        return True
    else:
        print("Your selection is not on the board or the space is occupied. Please try again\n")
        return False

def checkNotNumber(position):
    while True:
        try:
            x = int(position)
            # If there´s a bug it isn´t a number
        except ValueError:
                return True
        print("Only letters! Try again")
        return False

