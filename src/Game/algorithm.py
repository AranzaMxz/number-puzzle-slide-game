import time
from Game.aStar_algorithm import aStar

def algorithm(matrix, goalMatrix, goalsPositions):
    print("\t\n Better way\n")
    startTime = time.time()
    if not aStar(matrix, goalMatrix, goalsPositions):
          print("\nThere's no a solution\n")
    endTime = time.time ()
    totalTime = endTime - startTime
    print(f"Time to find a solution: {totalTime} second") 

    