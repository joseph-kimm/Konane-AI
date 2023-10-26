import random
import sys 
import copy

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

        #print("Move (" + str(r1) + "," + str(c1) + ") to (" + str(r2) + "," + str(c2) + ").")
        
        #print()
        
        # determine if moving X or O
        player = self.pieces[r1-1][c1-1]
        
        # removing the moved piece
        self.remove(r1, c1)

        # moving the piece
        self.pieces[r2-1][c2-1] = player
        self.empty.remove((r2-1, c2-1))

        #going down
        if (r1-r2 < 0):

            other_r = r1+ 1
            while other_r < r2:
                self.remove(other_r, c1)
                other_r += 2
            
        # going up
        if (r1-r2 > 0):

            other_r = r1 - 1
            while other_r > r2:
                self.remove(other_r, c1)
                other_r -= 2

        # going right
        if (c1-c2 < 0):

            other_c = c1+1
            while other_c < c2:
                self.remove(r1, other_c)
                other_c += 2

        # going left
        if (c1-c2 > 0):
            
            other_c = c1-1
            while other_c > c2:
                self.remove(r1, other_c)
                other_c -= 2

        
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
        
        # since our moves start from an empty piece, we cannot search for additional moves there
        # instead, we will consider all one jump moves and then see if there are additional moves to be made
        for move in OMoves:
            r1 = move[0][0]
            c1 = move[0][1]

            r2 = move[1][0]
            c2 = move[1][1]

            # move is to the right
            if (r1-r2 == -2):

                # finding all valid moves to the right
                while Board.isValid(r2+1, c1-1) and self.pieces[r2][c1-1] == 'X' and self.pieces[r2+1][c1-1] == '.':
                    OMoves.append([move[0], (r2+2, c1)])
                    r1 += 2
                    r2 += 2
                
            # move is to the left
            elif (r1-r2 == 2):

                # finding all valid moves to the left
                while Board.isValid(r2-3, c1-1) and self.pieces[r2-2][c1-1] == 'X' and self.pieces[r2-3][c1-1] == '.':
                    OMoves.append([move[0], (r2-2, c1)])
                    r1 -= 2
                    r2 -= 2
                
            # move is going down
            elif (c1-c2 == -2):

                # finding all valid moves going down
                while Board.isValid(r1-1, c2+1) and self.pieces[r1-1][c2] == 'X' and self.pieces[r1-1][c2+1] == '.':
                    OMoves.append([move[0], (r1, c2+2)])
                    c1 += 2
                    c2 += 2
                

            # move is going up
            elif (c1-c2 == 2):

                # finding all valid moves going up
                if Board.isValid(r1-1, c2-3) and self.pieces[r1-1][c2-2] == 'X' and self.pieces[r1-1][c2-3] == '.':
                    OMoves.append([move[0], (r1, c2-2)])
                    c1 -= 2
                    c2 -= 2

        return OMoves

    # returning list of possible moves for X
    # also includes multiple moves
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
            
        # since our moves start from an empty piece, we cannot search for additional moves there
        # instead, we will consider all one jump moves and then see if there are additional moves to be made
        for move in XMoves:
            r1 = move[0][0]
            c1 = move[0][1]

            r2 = move[1][0]
            c2 = move[1][1]

            # move is down
            if (r1-r2 == -2):

                # finding all valid moves down
                while Board.isValid(r2+1, c1-1) and self.pieces[r2][c1-1] == 'O' and self.pieces[r2+1][c1-1] == '.':
                    XMoves.append([move[0], (r2+2, c1)])
                    r1 += 2
                    r2 += 2
                
            # move is up
            elif (r1-r2 == 2):

                # finding all valid moves up
                while Board.isValid(r2-3, c1-1) and self.pieces[r2-2][c1-1] == 'O' and self.pieces[r2-3][c1-1] == '.':
                    XMoves.append([move[0], (r2-2, c1)])
                    r1 -= 2
                    r2 -= 2
                
            # move is right
            elif (c1-c2 == -2):

                # finding all valid moves to the right
                while Board.isValid(r1-1, c2+1) and self.pieces[r1-1][c2] == 'O' and self.pieces[r1-1][c2+1] == '.':
                    XMoves.append([move[0], (r1, c2+2)])
                    c1 += 2
                    c2 += 2
                

            # move is left
            elif (c1-c2 == 2):

                # finding all valid moves to the left
                if Board.isValid(r1-1, c2-3) and self.pieces[r1-1][c2-2] == 'O' and self.pieces[r1-1][c2-3] == '.':
                    XMoves.append([move[0], (r1, c2-2)])
                    c1 -= 2
                    c2 -= 2
        
        return XMoves


    
    def staticEvaluation(self):
        return len(self.listXMoves()) - len(self.listOMoves())

    # the minimax function
    # since the depth is in multiple of 2, even => computer (max), odd => user (min)
    # 
    @staticmethod
    def minimax(board, depth):

        # end, perform static evaluation
        if depth == 1:
            return (board.staticEvaluation(), board)

        # max node 
        if depth %2 == 0:
            moves = board.listXMoves()

            cbv = - sys.maxsize
            bestMove = ""

            for curMove in moves:
                next_board = copy.deepcopy(board)
                next_board.move(curMove[0][0], curMove[0][1], curMove[1][0], curMove[1][1])

                bv, move = Board.minimax(next_board, depth - 1)

                if bv > cbv:
                    cbv = bv
                    bestMove = next_board

            return (cbv, bestMove)

        # min node
        else:
            moves = board.listOMoves()
            cbv = sys.maxsize
            bestMove = ""
            
            for curMove in moves:
                next_board = copy.deepcopy(board)
                next_board.move(curMove[0][0], curMove[0][1], curMove[1][0], curMove[1][1])
  
                bv, move = Board.minimax(next_board, depth -1)
                if bv < cbv:
                    cbv = bv
                    bestMove = next_board

            return (cbv, bestMove)



# 1. how to find the move that computer made
# 2. issue of having no moves in minimax