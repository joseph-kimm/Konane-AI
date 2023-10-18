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


    
    