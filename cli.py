# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.
from logic import make_empty_board
from logic import update_board
from logic import get_winner
from logic import other_player
from logic import print_board
from logic import 

class Game:
    def __init__(self,playerO,playerX):
        self._board = Board()
        self._playerO = playerO
        self._playerX = playerX
    def run(self):
        while game_not_over:
            make_move(self._board, current_player)

class Human:
    def get_move(self,board):
        return parse_move(input())

class Bot:
    def get_move(self,board):
        return random_position(board)

game = Game(Human(),Bot())
game.run



if __name__ == '__main__':
    board = make_empty_board()
    winner = None
    current_player =input("Please input the first player(X or O):")
    print(print_board(board))
    while winner == None:
        target_position = input("Please input the position you want to put(eg: 13 for row 1 and col 3):")
        board = update_board(board,target_position,current_player)
        current_player = other_player(current_player)
        print("Take a turn, %s turn" %current_player)
        print(print_board(board))
        winner = get_winner(board)
        other_player(current_player)
    if winner == "X" or winner == "O":
        print("The winner is %s !" %winner)
    elif winner == "Draw":
        print("This game is draw!")
