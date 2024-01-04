# Konane-AI
Group project for CMSC B373, Introduction to Artificial Intelligence.

Contributors: Joseph Kim, Bridge Schaad.

# Description
Konane is a two-player, checkers-like board game from Hawaii. At the start of the game, checkers fill a grid in an alternating pattern with one cell removed. Players use black and white pieces. Black goes first and players take turns jumping the other's pieces. Double jumps in the same direction are allowed. The last player that can make a move wins.

This program enables users to play Konane on an 8x8 board against a computer, which utilizes a minimax algorithm. The pieces at (4,4) and (4,5) are removed at the start of the game, and players use X and O, rather than black and white pieces.

For more information about Konane, see [Anthropological Details of Konane](https://web.mit.edu/ieee/6.370/2001/web/konane-anthrop.html). 

# How to use
Use `python Konane.py` to play against a computer. The program will prompt all further game play.