class Board:
    def __init__(self, board, empty):
        self.board = board
        self.empty = empty


    def __init__(self):
        line1 = ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O']
        line2 = ['O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']

        board = []
        for i in range(4):
            board.append(line1)
            board.append(line2)

        self.board = board
        self.empty = []

    def print(self):
        print("  ", end="")
        for i in range(8):
            print(" " + str(i+1), end="")

        print("\n")

        for i in range(8):
            print(str(i+1) + " ", end="")

            for j in range(8):
                print(" " + self.board[i][j], end="")
            
            print()
        

    