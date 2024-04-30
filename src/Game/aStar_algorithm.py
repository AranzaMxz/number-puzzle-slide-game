import numpy as np
from Game.heuristic import heuristicFunc
from Game.Moves import generateMoves
from Board.matrix import printBoard

def aStar(start, goal, goalsPosition):
    cont = 0
    # Find the position of blank space
    blank_pos = np.where(matrix == "  ")
    

    # Saves the nodes to explore (state, g, h, path)
    openList = [(start, 0, heuristicFunc(start, goal, goalsPosition), None, blank_pos)]
    # Saves the expored nodes
    closeList = []

    # While there's nodes to explore  
    while openList:
        # x[1] -> g      x[2] -> h
        # f = g + h
        matrix, g, h, path, blank_pos= min(openList, key=lambda x: x[1] + x[2])
        if np.array_equal(matrix, goal): # We find a solution
            path = []
            while matrix is not None:
                path.append(matrix)
                matrix = next((node[3] for node in openList + closeList if np.array_equal(node[0], matrix)), None)
            for step in path[::-1]:
                cont += 1
                printBoard(len(step), step)
            print(f"\nTotal steps: {cont -1}")
            return True
        openList.remove((matrix,g,h, path, blank_pos)) # Removes the explored node
        closeList.append((matrix, g, h, path, blank_pos)) # adds the explored node

        # Generates all the paths from the current matrix
        for move in generateMoves(matrix, blank_pos):
            # We verificate the state is new or has being explored
            # if the x state is equals to state move -> true
            if not any(np.array_equal(x[0], move) for x in closeList):
                # g + 1 -> because we explored a new state
                openList.append((move, g+1, heuristicFunc(move, goal, goalsPosition), matrix, blank_pos))
                
    return False

