import unittest
from guessmynumber import guessmynumber


class GameTestCase(unittest.TestCase):
    """Test suite for Game class"""

    def setUp(self):
        self.game = guessmynumber.Game()

    def test_set_upper_bound(self):
        """Tests for set_upper_bound(difficulty)"""
        self.assertRaises(ValueError, self.game.set_upper_bound, '10')

        self.game.set_upper_bound('easy')
        self.assertEqual(self.game.upper_bound, 10, 'Should be 10')

        self.game.set_upper_bound('medium')
        self.assertEqual(self.game.upper_bound, 20, 'Should be 20')

        self.game.set_upper_bound('hard')
        self.assertEqual(self.game.upper_bound, 100, 'Should be 100')

        self.game.set_upper_bound('insane')
        self.assertEqual(self.game.upper_bound, 1000, 'Should be 1000')

    def test_check(self):
        """Tests for check(guess)"""
        self.game.secret_number = 10
        self.assertRaises(AssertionError, self.game.check, 'string')
        self.assertEqual(self.game.check(10), 0, 'Should return 0')
        self.assertEqual(self.game.check(15), 1, 'Should return 1')
        self.assertEqual(self.game.check(5), -1, 'Should return -1')


if __name__ == '__main__':
    unittest.main()
