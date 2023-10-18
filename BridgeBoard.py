class Board:
    def __init__(self):
        self.pieces = [['X' if (j+i+1)%2 == 1 else 'O' for i in range(8)] for j in range(8)]
        self.xCount = 31
        self.oCount = 31

    
    def print(self):
        print('   1  2  3  4  5  6  7  8')
        for i in range(8):
            print(i+1, end = "  ")
            for j in range(8):
                print(self.pieces[i][j], end = "  ")
            print()

    def remove(self, row, col):
        r = row-1
        c = col-1
        side = self.pieces[r][c]
        self.pieces[r][c] = "."
        if side == 'O':
            self.oCount= self.oCount - 1
        if side == 'X':
            self.xCount = self.xCount - 1

    def jump(self, row1, col1, row2, col2):
        r1 = row1 - 1
        c1 = col1 - 1
        r2 = row2 - 1
        c2 = col2 - 1
        if (self.pieces[r2][c2] != '.'):
            print("Please choose a valid jump")
            return
        if (r2 - r1 == 1): 
            self.pieces[r1+1][c1] = '.'

    def listOMoves(self):
        OMoves = []
        DIR1 = [[0,1], [0,-1], [-1, 0], [1, 0]]
        DIR2 = [[0,2], [0,-2], [-2,0], [2,0]]
        # find a '.' step
        for col in range(8):
            for row in range(8):
                if (self.pieces[col][row] == '.'):
                    for i in range(4):
                        if (row+DIR2[i][0]>=0 and row+DIR2[i][0]<=7) and (col+DIR2[i][1]>=0 and col+DIR2[i][1] <= 7):
                            #increment count wherever 'X' and 'O' in line
                            if (self.pieces[col+DIR1[i][1]][row+DIR1[i][0]] == 'X') and (self.pieces[col+DIR2[i][1]][row+DIR2[i][0]] == 'O'):
                                OMoves += ([[row+DIR2[i][0]+1, col+DIR2[i][1]+1], [row+1, col+1]])

        return OMoves 

    def listXMoves(self):
        XMoves = []
        DIR1 = [[0,1], [0,-1], [-1, 0], [1, 0]]
        DIR2 = [[0,2], [0,-2], [-2,0], [2,0]]
        # find a '.' step
        for row in range(8):
            for col in range(8):
                if (self.pieces[row][col] == '.'):
                    for i in range(4):
                        if (row+DIR2[i][0]>=0 and row+DIR2[i][0]<=7) and (col+DIR2[i][1]>=0 and col+DIR2[i][1] <= 7):
                            #increment count wherever 'X' and 'O' in line
                            if (self.pieces[row+DIR1[i][0]][col+DIR1[i][1]] == 'O') and (self.pieces[row+DIR2[i][0]][col+DIR2[i][1]] == 'X'):
                                XMoves += ([[row+DIR2[i][0]+1, col+DIR2[i][1]+1], [row+1, col+1]])

        return XMoves    

            

a = Board()
a.remove(4,5)
a.remove(4,4)
a.print()
print(a.listOMoves())
print(a.listXMoves())
#print(XMoves)