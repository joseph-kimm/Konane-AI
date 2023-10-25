import time
import random
from Board import Board

random.seed(time.clock())

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
        time.sleep(1)
        next = game.randomMove(moves)

        time.sleep(1)
        game.print()
        time.sleep(1)

        # checking if there are additional moves to be made
        while next:
            choice = random.randint(0,1)

            if choice == 0:
                next = move(next[0], next[1], next[2], next[3])
                time.sleep(1)
                print()
                game.print()
                time.sleep(1)
    
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

        next = game.move(moves[move][0][0], moves[move][0][1], moves[move][1][0], moves[move][1][1])

        time.sleep(1)
        game.print()
        time.sleep(1)

        # checking if there are additional moves to be made
        while next:
            play = input(f"Do you want to make another move from {(next[0], next[1])} to {(next[2], next[3])}? (y/n): ")
            if play == 'y':
                next = game.move(next[0], next[1], next[2], next[3])
                time.sleep(1)
                print()
                game.print()
                time.sleep(1)

    count += 1


    
    