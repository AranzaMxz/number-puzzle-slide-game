import numpy as np

def targetStatus(values):
    # Make the matrix an array
    matrixArray = np.array(values)
    
    # From array to list
    list_ = matrixArray.flatten()

    # We separate the blank space from the numbers
    blankSpace = list_[list_ == "  "] 
    numbers = list_[list_ != "  "]

    #  We sort the numbers ascending
    ordNumbers = np.sort(numbers)

    # We add the blank space to the numbers
    ordList = np.concatenate((ordNumbers, blankSpace))

    # We reshape the list to the original matrix size
    ordMatrix = ordList.reshape(matrixArray.shape)

    goalPositions = {}
    for i in range(len(ordMatrix)**2):
        # Convert i to string
        num = str(i) + "  "
        # Finds the positions of i 
        position = np.where(ordMatrix == num)
        goalPositions[num] = position


    #print(ordMatrix)
    return ordMatrix, goalPositions
