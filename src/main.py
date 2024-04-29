from Board.matrixInfo import getBoardSize
from Board.matrix import getBoard
from Data.insertNums import insert

print("\t---------------------------------------")
print("\n\t      N U M B E R   P U Z Z L E\n")
print("\t---------------------------------------\n")

# Get the board size
sizeBoard = getBoardSize()
# Print the board
values = getBoard(sizeBoard)

# Inserts the number in the position what the player wants
insert(values)


