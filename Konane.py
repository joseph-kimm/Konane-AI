import numpy as np
from Board import Board




a = Board()
a.remove(4,4)
a.print()
print(a.listOMoves())
print(a.listXMoves())
