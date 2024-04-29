import numpy as np

def checkInput(values, position):
    # The input is in the matrix 
    if np.any(values == position + " "):
        return True
    else:
        print("Your selection is not on the board or the space is occupied. Please try again\n")
        return False
'''
def isFree(values, position):
    if not np.any(values == position + " "):
        return False
    else:
        return True

'''

