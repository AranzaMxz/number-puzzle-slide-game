import numpy as np

def getValues(size):
    values = []
    numValues = size**2

    # Get the values 
    for i in range(numValues):
        values.append("X ")
    
    values = np.array(values)
    valuesMatrix = values.reshape(-1,size)

    #print(valuesMatrix)
    return valuesMatrix

def __printBoard(size, values):
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
                #        print("\t_ _ _", end="")
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
    #matrix = matrixCreate(size)
    values = getValues(size)
    __printBoard(size, values)
    #return matrix
