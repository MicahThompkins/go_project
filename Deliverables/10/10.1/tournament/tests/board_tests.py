sys.path.append('../')
from board import board
import unittest

# !!! testing board size is 19 !!!

class BoardTests(unittest.TestCase):

    def setUp(self):
        self.game_board = board([[" ", " ", "B", " ", " ", "W", "W", "W", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                                  [" ", " ", "W", "W", "W", " ", " ", "W", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                                  [" ", " ", "B", " ", "W", " ", " ", "W", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                                  [" ", " ", " ", " ", "W", " ", " ", "W", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                                  [" ", " ", " ", " ", "W", "W", "W", "W", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                                  [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                                  [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                                  [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                                  [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                                  [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                                  [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                                  [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                                  [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                                  [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                                  [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                                  [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                                  [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                                  [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                                  [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]])

    def test_occupies(self):
        self.assertTrue(self.game_board.occupies("W", "5-2"))
        self.assertFalse(self.game_board.occupies("B", "3-10"))
        self.assertTrue(self.game_board.occupies(" ", "19-1"))
        self.assertFalse(self.game_board.occupies("W", "3-1"))

    def test_occupied(self):
        self.assertTrue(self.game_board.occupied("5-3"))
        self.assertFalse(self.game_board.occupied("1-19"))

    def test_reachable(self):
        self.assertTrue(self.game_board.reachable("5-3", "B"))
        self.assertTrue(self.game_board.reachable("9-1", "B"))
        self.assertFalse(self.game_board.reachable("6-2", "B"))
        self.assertTrue(self.game_board.reachable("6-1", "B"))

    def test_place(self):
        self.assertEqual(self.game_board.place("B", "4-1"), [[" ", " ", "B", "B", " ", "W", "W", "W", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                                                              [" ", " ", "W", "W", "W", " ", " ", "W", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                                                              [" ", " ", "B", " ", "W", " ", " ", "W", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                                                              [" ", " ", " ", " ", "W", " ", " ", "W", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                                                              [" ", " ", " ", " ", "W", "W", "W", "W", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                                                              [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                                                              [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                                                              [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                                                              [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                                                              [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                                                              [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                                                              [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                                                              [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                                                              [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                                                              [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                                                              [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                                                              [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                                                              [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                                                              [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]])
        self.assertEqual(self.game_board.place("W", "3-1"), "This seat is taken!")
        self.assertEqual(self.game_board.place("B", "3-1"), "This seat is taken!")

    def test_remove(self):
        self.assertEqual(self.game_board.remove("B", "3-3"), [[" ", " ", "B", " ", " ", "W", "W", "W", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                                                              [" ", " ", "W", "W", "W", " ", " ", "W", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                                                              [" ", " ", " ", " ", "W", " ", " ", "W", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                                                              [" ", " ", " ", " ", "W", " ", " ", "W", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                                                              [" ", " ", " ", " ", "W", "W", "W", "W", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                                                              [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                                                              [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                                                              [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                                                              [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                                                              [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                                                              [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                                                              [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                                                              [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                                                              [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                                                              [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                                                              [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                                                              [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                                                              [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                                                              [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]])
        self.assertEqual(self.game_board.remove("W", "3-3"), "I am just a board! I cannot remove what is not there!")
        self.assertEqual(self.game_board.remove("W", "1-1"), "I am just a board! I cannot remove what is not there!")

    def test_get_points(self):
        self.assertEqual(self.game_board.get_points("W"), ["3-2", "4-2", "5-2", "5-3", "5-4", "5-5", "6-1", "6-5", "7-1", "7-5", "8-1", "8-2","8-3", "8-4", "8-5"])
        self.assertEqual(self.game_board.get_points("B"), ["3-1", "3-3"])
        self.assertEqual(board([["B", " ", "W", "W", "W", "B", "W", "B", "W", "B", "W", "B", "W", "B", "W", "B", "W", "W", " "],
                              ["B", "B", "W", "W", "W", "B", "W", "B", "W", "B", "W", "B", "W", "B", "W", "B", "W", "W", "B"],
                              ["B", "B", "W", "W", "W", "B", "W", "B", "W", "B", "W", "B", "W", "B", "W", "B", "W", "W", "B"],
                              ["B", "B", "W", "W", "W", "B", "W", "B", "W", "B", "W", "B", "W", "B", "W", "B", "W", "W", "B"],
                              ["B", "B", "W", "W", "W", "B", "W", "B", "W", "B", "W", "B", "W", "B", "W", "B", "W", "W", "B"],
                              ["B", "B", "W", "W", "W", "B", "W", "B", "W", "B", "W", "B", "W", "B", "W", "B", "W", "W", "B"],
                              ["B", "B", "W", "W", "W", "B", "W", "B", " ", "B", "W", "B", "W", "B", "W", "B", "W", "W", "B"],
                              ["B", "B", "W", "W", "W", "B", "W", "B", "W", "B", "W", "B", "W", "B", "W", "B", "W", "W", "B"],
                              ["B", "B", "W", " ", "W", "B", "W", "B", "W", "B", "W", "B", "W", "B", "W", "B", "W", "W", "B"],
                              ["B", "B", "W", "W", "W", "B", "W", "B", "W", "B", "W", "B", "W", "B", "W", "B", "W", "W", "B"],
                              ["B", "B", "W", "W", "W", "B", "W", "B", "W", "B", "W", "B", "W", "B", "W", "B", "W", "W", "B"],
                              ["B", "B", "W", "W", "W", "B", "W", "B", "W", "B", "W", "B", "W", "B", "W", "B", "W", "W", "B"],
                              ["B", "B", "W", "W", "W", "B", "W", "B", "W", "B", "W", "B", "W", "B", "W", "B", "W", "W", "B"],
                              ["B", "B", "W", "W", "W", "B", "W", "B", "W", "B", "W", "B", "W", "B", "W", "B", "W", "W", "B"],
                              ["B", "B", "W", "W", "W", "B", "W", "B", "W", "B", "W", "B", "W", "B", "W", "B", "W", "W", "B"],
                              ["B", "B", "W", "W", "W", "B", "W", "B", "W", "B", "W", "B", "W", "B", "W", "B", "W", "W", "B"],
                              ["B", "B", "W", "W", "W", "B", "W", "B", "W", "B", "W", "B", "W", "B", "W", "B", "W", "W", "B"],
                              ["B", "B", "W", "W", "W", "B", "W", "B", "W", "B", "W", "B", "W", "B", "W", "B", "W", "W", "B"],
                              ["B", "B", "W", "W", "W", "B", "W", "B", "W", "B", "W", "B", "W", "B", "W", "B", "W", "W", "B"]]).get_points(" "), ["19-1", "2-1", "4-9", "9-7"])



if __name__ == "__main__":
    unittest.main()
