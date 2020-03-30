import unittest
from game import Game

class GameTestCase(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        self.game.upper_bound = 20
        self.game.secret_number = 10

    # set_upper_bound() tests
    def test_set_upper_bound(self):
        self.assertRaises(ValueError, self.game.set_upper_bound, '10')

        self.game.set_upper_bound('easy')
        self.assertEqual(self.game.upper_bound, 10, 'Should be 10')

        self.game.set_upper_bound('medium')
        self.assertEqual(self.game.upper_bound, 20, 'Should be 20')

        self.game.set_upper_bound('hard')
        self.assertEqual(self.game.upper_bound, 100, 'Should be 100')

        self.game.set_upper_bound('insane')
        self.assertEqual(self.game.upper_bound, 1000, 'Should be 1000')

    # check() tests
    def test_check(self):
        self.assertRaises(AssertionError, self.game.check, 'string')
        self.assertEqual(self.game.check(10), 0, 'Should return 0')
        self.assertEqual(self.game.check(15), 1, 'Should return 1')
        self.assertEqual(self.game.check(5), -1, 'Should return -1')

if __name__ == '__main__':
    unittest.main()
