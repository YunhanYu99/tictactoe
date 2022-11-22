# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.
#from logic import *
from random import random

def make_empty_board():
    return [
        [None,None,None],
        [None,None,None],
        [None,None,None],
    ]

def game_type():
    game_type = int(input("Please input the number of the player(1 or 2):"))
    return game_type

class Game:
    def __init__(self):
        self.board = make_empty_board()
        self.player_number = game_type()
        if self.player_number == 1:
            #self.player_X = Human(1)
            #self.player_O = Bot(1)
            self.start_game()
        elif self.player_number == 2:
            self.player_X = Human(1)
            self.player_O = Human(2)
    
    def get_winner(self,Board):
        iswin = ""
        if Board[0][0] == Board[1][1] == Board[2][2] or Board[0][2] == Board[1][1] == Board[2][0]:
            iswin = Board[1][1]
        else:
            for i in range(0,3):
                if Board[i][0] == Board[i][1] == Board[i][2]:
                    iswin = Board[i][0]
                    break
                elif Board[0][i] == Board[1][i] == Board[2][i]:
                    iswin = Board[0][i]
                    break
        return iswin


    def game_state(self,winner,Board):
        iswin = winner
        if iswin == 'X' or iswin == 'O':
            return iswin
        elif (None in Board[0]) or (None in Board[1]) or (None in Board[2]):
            return None
        else:
            return 'Draw'

    def other_player(self, player):
        if player == 'X':
            return 'O'
        elif player == 'O':
            return 'X'

    def update_board(self,target_position,current_player):
        target_position_row = int(target_position[0])-1
        target_position_col = int(target_position[1])-1
        self.board[target_position_row][target_position_col] = current_player
        return self.board

    def print_board(self,board):
        output_board = ''
        for i in range(3):
            for j in range(3):
                if board[i][j] == None:
                    str_new = ' '
                else:
                    str_new = str(board[i][j])
                output_board = output_board + '|' + str_new 
            output_board = output_board + '|' + '\n'
            output_board = output_board + '-------'
            output_board = output_board + '\n'
        return output_board

    def start_game(self):#,board,current_player):
            board = make_empty_board()
            winner = None
            game_type = int(input("Please input the number of the player(1 or 2):"))
            if game_type == 2:
                current_player =input("Please input the first player(X or O):")
            else:
                current_player = 'O'
            print(self.print_board(board))
            while winner == None:
                target_position = input("Please input the position you want to put(eg: 13 for row 1 and col 3):")
                board = self.update_board(board,target_position,current_player)
                print(self.print_board(board))
                winner = self.get_winner(board)
                current_player = Player.other_player(current_player)
                if game_type == 1:
                    target_position = Human.get_move(board)
                    board = self.update_board(board,target_position,current_player)
                    print(self.print_board(board))
                    winner = self.get_winner(board)
                    current_player = Player.other_player(current_player)
                else:
                    print("Take a turn, %s turn" %current_player)
            if winner == "X" or winner == "O":
                print("The winner is %s !" %winner)
            elif winner == "Draw":
                print("This game is draw!")


class Player:
    def __init__(self,playername):
        self.playername = playername
    
    def first_player(self):
        first_player = input("Please in put the icon you want(X or O):")
        return first_player
    
    def other_player(self,player):
        if player == 'X':
            return 'O' # FIXME
        elif player == 'O':
            return 'X'

class Human(Player):
    def __init__(self,playername):
        self.playername = playername
        
    def get_move(self):
        target_position = input("Please input the position you want to put(eg: 13 for row 1 and col 3):")
        return target_position

class Bot(Player):
    def __init__(self,player):
        self.player = player

    def random_move(self,board):
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


if __name__ == '__main__':
    game = Game()


'''
Without OOP
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
'''