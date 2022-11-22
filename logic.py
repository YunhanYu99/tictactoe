# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.
def make_empty_board():
    return [
        [None,None,None],
        [None,None,None],
        [None,None,None],
    ]

def get_winner(Board):
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

    if iswin == 'X' or iswin == 'O':
        return iswin
    elif (None in Board[0]) or (None in Board[1]) or (None in Board[2]):
        return None
    else:
        return 'Draw'

def other_player(player):
    if player == 'X':
        return 'O' # FIXME
    elif player == 'O':
        return 'X'

def update_board(current_board,target_position,current_player):
    target_position_row = int(target_position[0])-1
    target_position_col = int(target_position[1])-1
    current_board[target_position_row][target_position_col] = current_player
    return current_board

'''
Original print board without change the None
def print_board(board):
    output_board = ''
    for i in range(3):
        for j in range(3):
            output_board = output_board+board[i][j]
        output_board = output_board + '\n'
    return output_board
    '''

def print_board(board):
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