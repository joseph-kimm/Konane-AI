import random

class Board:

    DIR1 = [[0,1], [0,-1], [-1, 0], [1, 0]]
    DIR2 = [[0,2], [0,-2], [-2,0], [2,0]]

    # initializing board with Xs and Os
    def __init__(self):
        self.pieces = [['X' if (j+i+1)%2 == 1 else 'O' for i in range(8)] for j in range(8)]
        self.empty = []

    # showing the current status of the board
    def print(self):
        print('   1  2  3  4  5  6  7  8')
        for row in range(8):
            print(row+1, end = "  ")
            for col in range(8):
                print(self.pieces[row][col], end = "  ")
            print()
        
    # removing a piece from the board
    def remove(self, row, col):
        r = row - 1
        c = col - 1
        self.pieces[r][c] = '.'
        self.empty.append((r, c))

    # Move a piece from start position (r1, c1) to end position at (r2, c2)
    def move(self, r1, c1, r2, c2):
        # determine if moving X or O
        player = self.pieces[r1][c1]
        
        self.remove(r1, c1)

        # Remove piece between start and end. Put player's piece at end position.
        if (r1-r2 == -2):
            self.remove(r1+1, c1)
            self.pieces[r2-1][c2-1] = player
        if (r1-r2 == 2):
            self.remove(r2+1, c1)
            self.pieces[r2-1][c2-1] = player
        if (c1-c2 == -2):
            self.remove(r1, c1+1)
            self.pieces[r2-1][c2-1] = player
        if (c1-c2 == 2):
            self.remove(r1, c2+1)
            self.pieces[r2-1][c2-1] = player

    # Pick a random move from the provided list
    def randomMove(self, list):
            idx = random.randint(0, len(list)-1)
            self.move(list[idx][0][0], list[idx][0][1], list[idx][1][0], list[idx][1][1])
        

    # checking if row and column is valid
    @staticmethod
    def isValid(row, col):
        if (row>=0 and row<=7) and (col>=0 and col <= 7):
            return True
        else:
            return False
        
    # returning list of possible moves for O
    def listOMoves(self):
        OMoves = []
        # find a '.' step
        for (r, c) in self.empty:
            for i in range(4):

                # row and column for DIR1, aka one block away
                row1 = r+self.DIR1[i][0]
                col1 = c+self.DIR1[i][1]

                # row and column for DIR2, aka two blocks away
                row2 = r+self.DIR2[i][0]
                col2 = c+self.DIR2[i][1]

                # checking if farther one is valdi
                if Board.isValid(row2, col2):

                    #increment count wherever 'X' and 'O' in line
                    if (self.pieces[row1][col1] == 'X') and (self.pieces[row2][col2] == 'O'):
                        OMoves.append([(row2+1, col2+1), (r+1, c+1)])
        return OMoves

    # returning list of possible moves for X
    def listXMoves(self):
        XMoves = []
        for (r, c) in self.empty:
            for i in range(4):
                
                # row and column for DIR1, aka one block away
                row1 = r+self.DIR1[i][0]
                col1 = c+self.DIR1[i][1]

                # row and column for DIR2, aka two blocks away
                row2 = r+self.DIR2[i][0]
                col2 = c+self.DIR2[i][1]

                # checking if farther one is valdi
                if Board.isValid(row2, col2):
                    
                    #increment count wherever 'X' and 'O' in line
                    if (self.pieces[row1][col1] == 'O') and (self.pieces[row2][col2] == 'X'):
                        XMoves.append([(row2+1, col2+1), (r+1, c+1)])

        return XMoves 