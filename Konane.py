import time
import random
from Board import Board
import copy
import sys 

random.seed(time.process_time())

count = 0
user = input("Do you want to play X or O? X goes first. (X/O): ")
if user == 'X':
    computer = 'O'
    count = 1
elif user == 'O':
    computer = 'X'

game = Board()
game.remove(4,4)
game.remove(4,5)
game.print()

while True:
    
    # computer's turn
    if count%2 == 0:

        moves = game.listMoves(computer)
        #print(moves)

        # check if game is over
        if len(moves) == 0:
            print("Player Won")
            exit()
        
        print("\nComputer's Turn: ", end = " ")


        bestVal = - sys.maxsize

        for move in moves:
            alpha = -1000
            beta = 1000
            temp = copy.deepcopy(game)
            temp.move(move[0][0], move[0][1], move[1][0], move[1][1])

            cbv = Board.minimax(temp, computer, 5, alpha, beta)
        
            if cbv > bestVal:
                bestVal = cbv
                bestMove = move

        print("Move " + str(bestMove[0]) + " to " + str(bestMove[1]))
        game.move(bestMove[0][0], bestMove[0][1], bestMove[1][0], bestMove[1][1])
    
    # player's turn
    else:
        moves = game.listMoves(user)

        # check if game is over
        if len(moves) == 0:
            print("Computer Won")
            exit()

        print("\nUser's Turn\n")

        # print all the available moves
        print("Available moves:")
        for i in range(len(moves)):
            print(str(i+1) + ") Move " + str(moves[i][0]) + " to " + str(moves[i][1]))

        move = int(input("\nEnter the number of the move that you want to make: ")) -1

        game.move(moves[move][0][0], moves[move][0][1], moves[move][1][0], moves[move][1][1])
        

    game.print()
    count += 1


    
    