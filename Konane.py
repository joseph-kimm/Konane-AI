import time
import random
from Board import Board

random.seed(time.process_time())

count = 0
game = Board()
game.remove(4,4)
game.remove(4,5)
game.print()

while True:
    
    # computer's turn
    if count%2 == 0:

        moves = game.listXMoves()

        # check if game is over
        if len(moves) == 0:
            print("Player Won")
            exit()
        
        print("\nComputer's Turn: ", end = " ")

        # pause, then make move
        cbv, bestBoard, chosen = Board.minimax(game, 4)
        print("Move " + str(chosen[0]) + " to " + str(chosen[1]))
        print(cbv)
        game = bestBoard
    
    # player's turn
    else:
        moves = game.listOMoves()

        # check if game is over
        if len(moves) == 0:
            print("Computer Won")
            exit()

        print("\nUser's Turn\n")

        # print all the available moves
        print("Available moves:")
        for i in range(len(moves)):
            print(str(i+1) + ") Move " + str(moves[i][0]) + " to " + str(moves[i][1]))

        move = int(input("Enter the number of the move that you want to make: ")) -1

        game.move(moves[move][0][0], moves[move][0][1], moves[move][1][0], moves[move][1][1])
        

    #time.sleep(1)
    game.print()
    #time.sleep(1)
    count += 1


    
    