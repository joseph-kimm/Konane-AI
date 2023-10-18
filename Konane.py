import numpy as np
from Board import Board


a = Board()
a.remove(4,4)
a.remove(4,5)
a.print()
print(a.listOMoves())
print(a.listXMoves())
a.randomMove(a.listXMoves())
a.print()

# while True:
#     print()
#     if (numO == 0):
#         print("You lose. Better luck next time.")
#         exit()
#     if (numX == 0):
#         print("You win! Congratulations!")
#         exit()

    
    