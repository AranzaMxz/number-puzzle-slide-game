from Game.Moves import generateMoves

def algorithm(values, targetMatrix):
     # We'll generate al possibles moves starting with the position of the blank space
     moves = generateMoves(values)
     print(moves)

    