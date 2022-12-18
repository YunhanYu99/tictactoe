import pandas as pd
games_filename = "/Users/yunhan/week5/tictactoe/game_record.csv"
move_filename = "/Users/yunhan/week5/tictactoe/move_record.csv"


def begin_data():
    try:
        return pd.read_csv(games_filename)
    except FileNotFoundError:
        return pd.DataFrame(columns=[
        "Game ID",
        "Player 1",
        "Player 2",
        "Winner",
    ])

def record_move():
    try:
        return pd.read_csv(move_filename)
    except FileNotFoundError:
        return pd.DataFrame(columns=[
        "Game ID",
        "Turn",
        "Player",
        "Position",
    ])

