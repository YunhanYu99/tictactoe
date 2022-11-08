

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
    if iswin == "None":
        iswin = None
    else:
        iswin = iswin
    return iswin

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
