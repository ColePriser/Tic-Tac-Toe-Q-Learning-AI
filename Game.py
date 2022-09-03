class Game:
    def __init__(self, display=True):
        # Displays grid if true, otherwise doesn't
        self.display = display

        # 3x3 grid for game
        self.grid = [[0, 0, 0] for _ in range(3)]

        # User is specified by 1, Agent is specified by -1
        self.cur_player = 1

        # Associate tic-tac-toe symbols with numbers for simplicity
        self.symbols = {1: "X", -1: "O", 0: "-"}

    def get_grid(self):
        # Returns the current grid
        return str(self.grid)

    def get_winner(self):
        # Checks if either player has won horizontally
        for row in range(3):
            if sum(self.grid[row]) == 3:
                return 1
                # If user has three in a row horizontally, return 1
            elif sum(self.grid[row]) == -3:
                return -1
                # If agent has three in a row horizontally, return -1

        # Checks if either player has won vertically
        for row in range(3):
            if sum(self.grid[row][col] for col in range(3)) == 3:
                return 1
                # If user has three in a row vertically, return 1
            elif sum(self.grid[row][col] for col in range(3)) == -3:
                return -1
                # If agent has three in a row vertically, return -1

        # Checks if either player has won diagonally
        if sum(self.grid[row][row] for row in range(3)) == 3:
            return 1
            # If user has three in a row diagonally, return 1
        elif sum(self.grid[row][row] for row in range(3)) == -3:
            return -1
            # If agent has three in a row diagonally, return -1

        return 0
        # If no player has won, then return 0

    def get_available_points(self):
        # Return array of locations that don't have X or O
        available = []
        for row in range(3):
            for col in range(3):
                if self.grid[row][col] == 0:
                    available.append[row][col]
        return available

    def full_grid(self):
        # If every location has an X or O, then return True
        for row in range(3):
            for col in range(3):
                if self.grid[row][col] == 0:
                    return False
        return True

    def _print_grid(self):
        # Print the current grid
        for row in self.grid:
            for cur in row:
                print(self.symbols[cur], end="\t")
            print("\n")
        print("________________\n")

    def play(self, row, col):
        if self.grid[row][col] != 0:
            return None
            # If the desired location is taken, return None
        # Otherwise, assign desired location to current player number
        self.grid[row][col] = self.cur_player
        if self.display:
            self._print_grid()
            # If display is true, then print the current grid

        if self.get_winner() == 1:
            return 1
            # If user has won, then return 1
        elif self.get_winner() == -1:
            return -1
            # If agent has won, then return -1
        # Change current player
        self.cur_player *= -1
        return None

