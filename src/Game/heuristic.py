import numpy as np

# Manhattan distance
# f = h + g
# Check the differences between the actual state and the goal
def heuristicFunc(matrix, goal, goalsPosition):
    distance = 0
    # We go through the actual matrix and compare with the goal matrix
    for i in range(len(matrix)**2):
        # Finds the position of the number in the current matrix
        actualPos = np.where(matrix == str(i) + "  ")
        # Finds the position of the number in the goal matrix using the dictionary
        goalPos = goalsPosition[str(i) + "  "]
        distance += abs(actualPos[0] - goalPos[0]) + abs(actualPos[1] + goalPos[1])
    return distance
