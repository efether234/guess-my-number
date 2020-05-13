import unittest
from guessmynumber.game import Game


class GameTestCase(unittest.TestCase):
    """Test suite for Game class"""
    def setUp(self):
        self.game = Game('hard')

    def test_check(self):
        """Tests for check(guess)"""
        self.assertRaises(AssertionError, self.game.check, 'string')
        self.assertEqual(self.game.check(
            self.game.secret_number), 0, 'Should return 0')
        self.assertEqual(self.game.check(
            self.game.secret_number + 1), 1, 'Should return 1')
        self.assertEqual(self.game.check(
            self.game.secret_number - 1), -1, 'Should return -1')


if __name__ == '__main__':
    unittest.main()
