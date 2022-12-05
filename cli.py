# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.
#from logic import *
# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.

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
            self.start_game(1,self.board)
        elif self.player_number == 2:
            self.start_game(2,self.board)
    
    def get_winner(self,Board):
        iswin = None
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

    def update_board(self,board,target_position,current_player):
        target_position_row = int(target_position[0])-1
        target_position_col = int(target_position[1])-1
        board[target_position_row][target_position_col] = current_player
        return board

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

    def first_player(self):
        first_player = input("Please in put the icon you want(X or O):")
        return first_player
    
    def other_player(self,player):
        if player == 'X':
            return 'O' # FIXME
        elif player == 'O':
            return 'X'

    def start_game(self,game_type,board):
            board = self.board
            winner = None
            if game_type == 2:
                current_player = self.first_player()
            else:
                current_player = 'O'
            #print board
            print(self.print_board(board))
            while winner == None:
                #get move
                human = Human()
                target_position = human.get_move()
                #update & print board
                board = self.update_board(board,target_position,current_player)
                print(self.print_board(board))
                #get winner
                is_win = self.get_winner(board)
                winner = self.game_state(is_win,board)
                if winner == None:
                    # Robot player
                    if game_type == 1:
                        current_player = self.other_player(current_player)
                        bot = Bot()
                        target_position = bot.random_move(board)
                        board = self.update_board(board,target_position,current_player)
                        print(self.print_board(board))
                        is_win = self.get_winner(board)
                        winner = self.game_state(is_win,board)
                        print(winner)
                        current_player = self.other_player(current_player)
                    # Human player
                    else:
                        current_player = self.other_player(current_player)
                        print("Take a turn, %s turn" %current_player)
            if winner == "X" or winner == "O":
                print("The winner is %s !" %winner)
            elif winner == "Draw":
                print("This game is draw!")


                
class Human():
    def __init__(self):
        super().__init__()
        return None
        
    def get_move(self):
        target_position = input("Please input the position you want to put(eg: 13 for row 1 and col 3):")
        return target_position

class Bot():
    def __init__(self):
        super().__init__()
        return None

    def random_move(self,board):
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
