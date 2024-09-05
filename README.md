# Tic-Tac-Toe Game

<img src="https://github.com/user-attachments/assets/ade253d2-7faf-4e3f-9315-dac1d94f7c5e" alt="Tic Tac Toe" width="400"/>

## Overview
This repository contains two versions of a simple Tic-Tac-Toe game implemented in Python. The two versions are:
- **Human vs. Human (ttt_hvh.py):** A two-player version where both players are human and take turns entering their moves.
- **Human vs. Computer (ttt_hvc.py):** A version where one player is human, and the other is controlled by the computer, which makes random moves.

# Game Rules
- The game board consists of a 3x3 grid, with each cell being either empty (_), marked with an X, or marked with an O.
- Players take turns to mark a cell.
- The first player to get three of their marks in a row, either horizontally, vertically, or diagonally, wins the game.
- If all cells are filled and no player has won, the game ends in a tie.

# Code Explanation
- printBoard(board): Prints the current state of the board.
- playerInput(board): Takes input from the player and updates the board.
- checkHorizontal(board): Checks for a win condition in horizontal lines.
- checkVertically(board): Checks for a win condition in vertical lines.
- checkDiagonally(board): Checks for a win condition in diagonals.
- checkTie(board): Checks if the game has ended in a tie.
- checkWin(): Checks if there is a winner or if the game has ended.
- switchPlayer(): Switches the current player between X and O.
- computer(board): Makes a random move for the computer player (in the Human vs. Computer version).
