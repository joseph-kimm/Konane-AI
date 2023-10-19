from Board import Board

count = 0
game = Board()
game.remove(4,4)
game.remove(4,5)
game.print()

while True:
    
    # computer's turn
    if count%2 == 0:

        print("\nComputer's Turn\n")
        moves = game.listXMoves()

        # check if game is over
        if len(moves) == 0:
            print("Player Won")
            exit()
        
        game.randomMove(moves)
    
    # player's turn
    else:
        print("\nUser's Turn\n")
        moves = game.listOMoves()

        # check if game is over
        if len(moves) == 0:
            print("Computer Won")

        # print all the available moves
        print("Available moves:")
        for i in range(len(moves)):
            print(str(i+1) + ") Move " + str(moves[i][0]) + " to " + str(moves[i][1]))

        move = int(input("Enter the number of the move that you want to make: ")) -1

        print(moves[move][0][0], moves[move][0][1], moves[move][1][0], moves[move][1][1])

        game.move(moves[move][0][0], moves[move][0][1], moves[move][1][0], moves[move][1][1])
    
    game.print()
    count += 1


    
    