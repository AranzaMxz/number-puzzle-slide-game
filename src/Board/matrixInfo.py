
# Verificate the input is allow
def getBoardSize():
    while True:
        try:
            size = int(input("Write the board size (min 2 - max 7): "))
            if size < 2:   
                print("The minium is 2. Try again\n")
            elif size > 7:
                print("The maximum is 7. Try again\n")
            else:
                return size
        except ValueError:
            print("That´s not allow! Try again")