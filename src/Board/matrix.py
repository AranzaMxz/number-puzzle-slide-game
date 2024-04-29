import numpy as np
import string

def getValues(size):
    values = []
    numValues = size**2
    alphabet = string.ascii_lowercase + string.ascii_uppercase

    # Get the values 
    for i in range(numValues):
        # Insert the alphabet
        values.append(alphabet[i % len(alphabet)] + " ")
    
    values = np.array(values)
    valuesMatrix = values.reshape(-1,size)

    #print(valuesMatrix)
    return valuesMatrix

def printBoard(size, values):
    print("\n")
    for i in range(size):
        if i == 0 :
            for j in range(size):
                if j == 0:
                    print("\t", end="")
                if j == size-1:
                    print(" _ _ _", end="")
                else:
                    print(" _ _ _ _ _", end="")
        print()
        for j in range(size+1):
            if j == 0:
                print("\t", end="")
            print("|        ", end="")
        print()
        for j in range(size + 1):
            if j == 0:
                print("\t", end="")
            if j == size-1:
                print("|   {}   |".format(values[i][j]), end="")  
            elif j != size:
                print("|   {}   ".format(values[i][j]), end="")
        print()
        for j in range(size + 1):
            #print(j)
            if j == 0:
                print("\t", end="")
            #print("_ _ _ _ _|", end="")
            if j == size:
                print("|", end="")
            else:
                print("|_ _ _ _ ", end="")
    print("\n")
            

def getBoard(size):
    values = getValues(size)
    printBoard(size, values)
    return values
