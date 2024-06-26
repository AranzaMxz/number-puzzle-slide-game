import numpy as np

class Node: # Define a state of the table as a node
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action

class StackFrontier: # Set a stack for the possible nodes to search the solution
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any((node.state[0] == state[0]).all() for node in self.frontier)
    
    def empty(self):
        return len(self.frontier) == 0
    
    def remove(self):
        if self.empty():
            raise Exception("Empty Frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node

class QueueFrontier(StackFrontier): # Manage the stack as a queue
    def remove(self):
        if self.empty():
            raise Exception("Empty Frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node

class Puzzle: # Like a main class that defines the game and the solution to this, setting the neighbors as the possible movements of the blank box
    def __init__(self, start, startIndex, goal, goalIndex):
        self.start = [start, startIndex]
        self.goal = [goal, goalIndex]
        self.solution = None
        self.explored = set()

    def neighbors(self, state):
        mat, (row, col) = state
        results = []
        
        if row > 0:
            mat1 = np.copy(mat)
            mat1[row][col] = mat1[row - 1][col]
            mat1[row - 1][col] = 0
            results.append(('up', [mat1, (row - 1, col)]))
        if col > 0:
            mat1 = np.copy(mat)
            mat1[row][col] = mat1[row][col - 1]
            mat1[row][col - 1] = 0
            results.append(('left', [mat1, (row, col - 1)]))
        if row < 2:
            mat1 = np.copy(mat)
            mat1[row][col] = mat1[row + 1][col]
            mat1[row + 1][col] = 0
            results.append(('down', [mat1, (row + 1, col)]))
        if col < 2:
            mat1 = np.copy(mat)
            mat1[row][col] = mat1[row][col + 1]
            mat1[row][col + 1] = 0
            results.append(('right', [mat1, (row, col + 1)]))

        return results

    def state_to_tuple(self, state):
        """Convert state array to a tuple for hashing."""
        return tuple(map(tuple, state[0]))

    def solve(self):
        self.num_explored = 0

        start = Node(state=self.start, parent=None, action=None)
        frontier = QueueFrontier()
        frontier.add(start)
        self.explored.add(self.state_to_tuple(start.state))  # Hash initial state

        while True:
            if frontier.empty():
                raise Exception("No solution")

            node = frontier.remove()
            self.num_explored += 1

            if (node.state[0] == self.goal[0]).all():
                actions = []
                cells = []
                while node.parent is not None:
                    actions.append(node.action)
                    cells.append(node.state)
                    node = node.parent
                actions.reverse()
                cells.reverse()
                self.solution = (actions, cells)
                return

            for action, state in self.neighbors(node.state):
                state_tuple = self.state_to_tuple(state)
                if not frontier.contains_state(state) and state_tuple not in self.explored:
                    child = Node(state=state, parent=node, action=action)
                    frontier.add(child)
                    self.explored.add(state_tuple)

            print(f"Explored: {self.num_explored} states")

    def print_solution(self):
        if self.solution:
            print("Start State:\n", self.start[0], "\n")
            print("Goal State:\n",  self.goal[0], "\n")
            print("\nStates Explored: ", len(self.explored), "\n")
            print("Solution:\n ")
            for action, cell in zip(self.solution[0], self.solution[1]):
                print("action: ", action, "\n", cell[0], "\n")
            print("Goal Reached!!")
        else:
            print("No solution found.")

def start_matrix(size): # Method for the initaialization of the start state of the matrix 
    matrix = []
    used_numbers = set()

    for i in range(size):
        row = []
        for j in range(size):
            while True:
                try:
                    number = int(input(f"Enter a number between 0-8 for position ({i},{j}) (No repeat): "))
                    if number in used_numbers:
                        print("Number already used. Try again.")
                    elif 0 <= number <= 8:
                        row.append(number)
                        used_numbers.add(number)
                        break
                    else:
                        print("Invalid number. Number must be between 0 and 8.")
                except ValueError:
                    print("Invalid input. Please enter an integer.")
                    
        matrix.append(row)

    return np.array(matrix)

# Setting some parameters as statics variables, it may be dinamically changed if is required
size = 3 # Size of the board
start = start_matrix(size) # Start state of the board matrix
goal = np.array([[1,2,3],[4,5,6],[7,8,0]]) # State of the board to achieve

start_zero_Index = (int(np.where(start == 0)[0][0]), int(np.where(start == 0)[1][0])) # Start posotion of the blank box
goal_zero_Index = (2, 2) # Goal position of the blank box

p = Puzzle(start, start_zero_Index, goal, goal_zero_Index) # Variable to start the game
p.solve() # Runs the solve method that stores the solution if exists
p.print_solution() # Print the solution found in the last Method
