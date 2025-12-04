import unittest
import Connect4


class TestCheckWinner(unittest.TestCase):
    def test_no_winner_on_empty_board(self):
        game = Connect4.Connect4(None)
        self.assertIsNone(game.check_winner())
        self.assertFalse(game.game_over)
        self.assertIsNone(game.winner)

    def test_vertical_win(self):
        game = Connect4.Connect4(None)
        for _ in range(4):
            self.assertTrue(game.take_action(("x", 0)))

        self.assertEqual(game.check_winner(), "x")
        self.assertTrue(game.game_over)
        self.assertEqual(game.winner, "x")

    def test_horizontal_win(self):
        game = Connect4.Connect4(None)
        for col in range(4):
            self.assertTrue(game.take_action(("x", col)))

        self.assertEqual(game.check_winner(), "x")
        self.assertTrue(game.game_over)
        self.assertEqual(game.winner, "x")

    def test_diagonal_down_right_win(self):
        game = Connect4.Connect4(None)

        # Build diagonal from (0,0) to (3,3)
        game.take_action(("x", 0))  # (0,0)

        game.take_action(("o", 1))  # (1,0)
        game.take_action(("x", 1))  # (1,1)

        game.take_action(("o", 2))  # (2,0)
        game.take_action(("o", 2))  # (2,1)
        game.take_action(("x", 2))  # (2,2)

        game.take_action(("o", 3))  # (3,0)
        game.take_action(("o", 3))  # (3,1)
        game.take_action(("o", 3))  # (3,2)
        game.take_action(("x", 3))  # (3,3)

        self.assertEqual(game.check_winner(), "x")
        self.assertTrue(game.game_over)
        self.assertEqual(game.winner, "x")

    def test_diagonal_up_right_win(self):
        game = Connect4.Connect4(None)

        # Build diagonal from (0,3) up-right to (3,0)
        game.take_action(("x", 3))  # (3,0)

        game.take_action(("o", 2))  # (2,0)
        game.take_action(("x", 2))  # (2,1)

        game.take_action(("o", 1))  # (1,0)
        game.take_action(("o", 1))  # (1,1)
        game.take_action(("x", 1))  # (1,2)

        game.take_action(("o", 0))  # (0,0)
        game.take_action(("o", 0))  # (0,1)
        game.take_action(("o", 0))  # (0,2)
        game.take_action(("x", 0))  # (0,3)

        self.assertEqual(game.check_winner(), "x")
        self.assertTrue(game.game_over)
        self.assertEqual(game.winner, "x")


if __name__ == "__main__":
    unittest.main()
