import unittest
import logic

#TODO: Test all function from logic.py!

class TestLogic(unittest.TestCase):
    def test_get_winner(self):
        board_1 = [
            ['X',None,'O'],
            [None,'X',None],
            [None,'O','X'],
        ]
        board_2 = [
        [None,None,None],
        [None,None,None],
        [None,None,None],
        ]
        board_3 = [
            ['O',None,'O'],
            [None,'O',None],
            [None,'O','X'],            
        ]
        board_4 = [
            ['O',None,'O'],
            [None,'O','X'],
            [None,'O','O'],            
        ]
        self.assertEqual(logic.get_winner(board_1),'X')
        self.assertEqual(logic.get_winner(board_2),None)
        self.assertEqual(logic.get_winner(board_3),None)
        self.assertEqual(logic.get_winner(board_4),'O')

    def test_make_empty_board(self):
        self.assertEqual(logic.make_empty_board(),[
        [None,None,None],
        [None,None,None],
        [None,None,None],
        ])

    def test_other_player(self):
        current_player_X = "X"
        current_player_O = "O"
        self.assertEqual(logic.other_player(current_player_X),"O")
        self.assertEqual(logic.other_player(current_player_O),"X")

    def update_board(self):
        current_board = [
        ["X","O","O"],
        [None,"X",None],
        [None,None,None],
        ]
        target_position = '23'
        current_player = 'O'
        self.assertEqual(logic.other_player(current_board,target_position,current_player),
        [
        ["X","O","O"],
        [None,"X","O"],
        [None,None,None],
        ])


if __name__ == '__main__':
    unittest.main()