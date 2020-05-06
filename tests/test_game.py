import unittest
from guessmynumber import guessmynumber


class GameTestCase(unittest.TestCase):
    """Test suite for Game class"""
    def setUp(self):
        self.game = guessmynumber.Game('hard')

    def test_check(self):
        """Tests for check(guess)"""
        self.game.secret_number = 10
        self.assertRaises(AssertionError, self.game.check, 'string')
        self.assertEqual(self.game.check(10), 0, 'Should return 0')
        self.assertEqual(self.game.check(15), 1, 'Should return 1')
        self.assertEqual(self.game.check(5), -1, 'Should return -1')


if __name__ == '__main__':
    unittest.main()
