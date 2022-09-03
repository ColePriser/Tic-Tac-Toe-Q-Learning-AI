class Game:
    def __init__(self, display=True):
        # Displays grid if true, otherwise doesn't
        self.display = display

        # 3x3 grid for game
        self.grid = [[0, 0, 0] for _ in range(3)]

        # User is specified by 1, Agent is specified by -1
        self.player = 1

        # Associate tic-tac-toe symbols with numbers for simplicity
        self.symbols = {1: "X", -1: "O", 0: "-"}

    def get_grid(self):
        # Returns the current grid
        return str(self.grid)

    def get_winner(self):
        # Checks if either player has won horizontally
        for x in range(3):
            if sum(self.grid[x]) == 3:
                return 1
                # If user has three in a row horizontally, return 1
            elif sum(self.grid[x]) == -3:
                return -1
                # If agent has three in a row horizontally, return -1

        # Checks if either player has won vertically
        for x in range(3):
            if sum(self.grid[x][y] for y in range(3)) == 3:
                return 1
                # If user has three in a row vertically, return 1
            elif sum(self.grid[x][y] for y in range(3)) == -3:
                return -1
                # If agent has three in a row vertically, return -1

        # Checks if either player has won diagonally
        if sum(self.grid[x][x] for x in range(3)) == 3:
            return 1
            # If user has three in a row diagonally, return 1
        elif sum(self.grid[x][x] for x in range(3)) == -3:
            return -1
            # If agent has three in a row diagonally, return -1

        return 0
        # If no player has won, then return 0

