# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.
from logic import *


'''
class Game:
    def __init__(self,playerO,playerX):
        self._board = Board()
        self._playerO = playerO
        self._playerX = playerX

    def game_not_over(self):


    def run(self):
        while game_not_over:
            make_move(self._board, current_player)
        
    


class Board:
    "The game board of the tic-tac-toe game"
    def __init__(self):
        self.board = [
        [None,None,None],
        [None,None,None],
        [None,None,None],
            ]
    
    def print_format_board(self):
        output_board = ''
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == None:
                    str_new = ' '
                else:
                    str_new = str(self.board[i][j])
                output_board = output_board + '|' + str_new 
            output_board = output_board + '|' + '\n'
            output_board = output_board + '-------'
            output_board = output_board + '\n'
        return print(output_board)

    def update_board(self,target_position,current_player):
        target_position_row = int(target_position[0])-1
        target_position_col = int(target_position[1])-1
        self.board[target_position_row][target_position_col] = current_player
        return self.board


class Human:
    def get_move(self):
        target_position = input("Please input the position you want to put(eg: 13 for row 1 and col 3):")
        return target_position

class Bot:
    def get_move(board):
        import random
        target_row = 4
        target_col = 4
        while target_row == 4 or target_col == 4:
            row = random.randint(1,3) #same as the input with the user row 1-3 and col 1-3
            col = random.randint(1,3)
            if board[row-1][col-1] == None:
                target_row = row
                target_col = col
        target_position = str(target_row)+str(target_col)
        return target_position

game = Game(Human(),Bot())
game.run
'''


if __name__ == '__main__':
    board = make_empty_board()
    winner = None
    game_type = int(input("Please input the number of the player(1 or 2):"))
    if game_type == 2:
        current_player =input("Please input the first player(X or O):")
    else:
        current_player = 'O'
    print(print_board(board))
    while winner == None:
        target_position = input("Please input the position you want to put(eg: 13 for row 1 and col 3):")
        board = update_board(board,target_position,current_player)
        print(print_board(board))
        winner = get_winner(board)
        current_player = other_player(current_player)
        if game_type == 1:
            target_position = get_move(board)
            board = update_board(board,target_position,current_player)
            print(print_board(board))
            winner = get_winner(board)
            current_player = other_player(current_player)
        else:
            print("Take a turn, %s turn" %current_player)
    if winner == "X" or winner == "O":
        print("The winner is %s !" %winner)
    elif winner == "Draw":
        print("This game is draw!")
