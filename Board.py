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
        temp = self.pieces[r][c]
        self.pieces[r][c] = '.'
        self.empty.append((r, c))
        return temp

    # Move a piece from start position (r1, c1) to end position at (r2, c2)
    def move(self, r1, c1, r2, c2):
        print("Move (" + str(r1) + "," + str(c1) + ") to (" + str(r2) + "," + str(c2) + ").")
        print()

        # determine if moving X or O
        player = self.pieces[r1-1][c1-1]
        
        # removing the moved piece
        self.remove(r1, c1)

        # moving the piece
        self.pieces[r2-1][c2-1] = player
        self.empty.remove((r2-1, c2-1))

        # Remove piece between start and end. Put player's piece at end position.

        #going right
        if (r1-r2 == -2):
            other = self.remove(r1+1, c1)

            # there is another valid move to the right
            if Board.isValid(r2+1, c1-1) and self.pieces[r2][c1-1] == other and self.pieces[r2+1][c1-1] == '.':
                return [r2, c1, r2+2, c1]
            else:
                return None
            
        # going left
        if (r1-r2 == 2):
            other = self.remove(r2+1, c1)

            # there is another valid move to the left
            if Board.isValid(r2-3, c1-1) and self.pieces[r2-2][c1-1] == other and self.pieces[r2-3][c1-1] == '.':
                return [r2, c1, r2-2, c1]
            
            # there is no other valid move to the left
            else:
                return None

        # going down
        if (c1-c2 == -2):
            other = self.remove(r1, c1+1)

            # there is another valid moving down
            if Board.isValid(r1-1, c2+1) and self.pieces[r1-1][c2] == other and self.pieces[r1-1][c2+1] == '.':
                return [r1, c2, r1, c2+2]
            
            # there is no other valid moving down
            else:
                return None

        # going up
        if (c1-c2 == 2):
            other = self.remove(r1, c2+1)

            # there is another valid moving up
            if Board.isValid(r1-1, c2-3) and self.pieces[r1-1][c2-2] == other and self.pieces[r1-1][c2-3] == '.':
                return [r1, c2, r1, c2-2]
            
            # there is no other valid moving up
            else:
                return None
        
    # Pick a random move from the provided list
    def randomMove(self, list):
            idx = random.randint(0, len(list)-1)
            moves = self.move(list[idx][0][0], list[idx][0][1], list[idx][1][0], list[idx][1][1])
            return moves
        

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

                # checking if farther one is valid
                if Board.isValid(row2, col2):
                    
                    #increment count wherever 'X' and 'O' in line
                    if (self.pieces[row1][col1] == 'O') and (self.pieces[row2][col2] == 'X'):
                        XMoves.append([(row2+1, col2+1), (r+1, c+1)])

        return XMoves 