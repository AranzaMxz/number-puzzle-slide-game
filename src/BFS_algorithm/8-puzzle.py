import numpy as np

class Node:
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action

class StackFrontier:
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

class QueueFrontier(StackFrontier):
    def remove(self):
        if self.empty():
            raise Exception("Empty Frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node

class Puzzle:
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

            # Debug print to monitor progress
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

def create_user_defined_matrix(size):
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

size = 3
start = create_user_defined_matrix(size)
goal = np.array([[1,2,3],[4,5,6],[7,8,0]])

startIndex = (int(np.where(start == 0)[0][0]), int(np.where(start == 0)[1][0]))
goalIndex = (2, 2)

p = Puzzle(start, startIndex, goal, goalIndex)
p.solve()
p.print_solution()
