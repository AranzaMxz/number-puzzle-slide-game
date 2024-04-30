import numpy as np
import heapq
from Game.heuristic import heuristicFunc
from Game.Moves import generateMoves
from Board.matrix import printBoard

def aStar(start, goal, goalsPosition):
    cont = 0
    # Find the position of blank space
    blank_pos = np.where(start == "  ")
    

    # Saves the nodes to explore (state, g, h, path)
    openList = [(0, 0, heuristicFunc(start, goal, goalsPosition), start, [], blank_pos)]
    heapq.heapify(openList) # converts the openList to a heap
    # Saves the expored nodes
    closeList = set()

    # While there's nodes to explore  
    while openList:
        # x[1] -> g      x[2] -> h
        # f = g + h
        _, g, h, matrix, path, blank_pos = heapq.heappop(openList)  # Pop the node with the smallest f value

        if np.array_equal(matrix, goal): # We find a solution
            path.append(matrix)
            for i, step in enumerate(path):
                if i == 0:
                    print("\t     Start", end="")
                else:
                    cont += 1
                    print(f"\t     Step {cont}", end="")
                printBoard(len(start), step)
            print(f"Total steps: {cont}")
            return True
        #openList.remove((matrix,g,h, path, blank_pos)) # Removes the explored node
        closeList.add(tuple(matrix.flatten())) # adds the explored node

        # Generates all the paths from the current matrix
        for move in generateMoves(matrix, blank_pos):
            # We verificate the state is new or has being explored
            # if the x state is equals to state move -> true
            if tuple(move.flatten()) not in closeList:
                new_blank_pos = np.where(move == "  ")
                f = g + 1 + heuristicFunc(move, goal, goalsPosition)
                newPath = path.copy()
                newPath.append(matrix) # Adds the matrix as a new way
                # g + 1 -> because we explored a new state
                heapq.heappush(openList, (f, g+1, heuristicFunc(move, goal, goalsPosition), move, newPath, new_blank_pos))
                
    return False

