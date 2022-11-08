# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.
from logic import make_empty_board
from logic import update_board
from logic import get_winner
from logic import other_player

if __name__ == '__main__':
    board = make_empty_board()
    winner = None
    current_player =input("Please input the first player(X or O):")
    while winner == None:
        target_position = input("Please input the position you want to put(eg: 13 for row 1 and col 3):")
        update_board(board,target_position,current_player)
        current_player = other_player(current_player)
        print("Take a turn, %s turn",current_player)
        
        # TODO: Show the board to user.
        # TODO: Input a move from the player.
        # TODO: Update the board.

        winner = get_winner(board)
        other_player(current_player)
    winner = 'X' # FIXMEh