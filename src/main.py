from Board.matrixInfo import getBoardSize
from Board.matrix import getBoard
from Data.insertNums import insert
from Data.idealState import targetStatus
from Game.algorithm import algorithm

print("\t---------------------------------------")
print("\n\t N U M B E R   P U Z Z L E   S L I D E\n")
print("\t---------------------------------------\n")

# Get the board size
sizeBoard = getBoardSize()
# Print the reference board
X_values = getBoard(sizeBoard)

# Inserts the number in the position what the player wants
values = insert(X_values)

targetMatrix = targetStatus(values)

algorithm(values,targetMatrix)


