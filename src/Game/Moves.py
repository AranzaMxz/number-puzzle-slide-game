import numpy as np

def generateMoves(matrix, blank_pos):
    

    moves = [] # Save all the possibles matrix generate of move tha blank space

    # All the directions we can go: up, down, left and right
    directions = [(-1,0), (1,0), (0,-1), (0,1)]

    for x, y in directions:
        # blank_pos = (x, y)
        newPos = (blank_pos[0] + x, blank_pos[1] + y)
        # Verificates the new pos is on the range and it´s a validated position
        if 0 <= newPos[0] < len(matrix) and 0 <= newPos[1] < len(matrix):
            newMatrix = matrix.copy() # Copy the matrix because we don't modificate the original
            # We change the positions
            newMatrix[blank_pos], newMatrix[newPos] = newMatrix[newPos], newMatrix[blank_pos]
            moves.append(newMatrix) # Add the new matrix copy to the list of moves
    return moves
