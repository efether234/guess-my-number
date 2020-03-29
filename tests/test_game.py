import unittest
from guess_my_number import Game

class GameTestCase(unittest.TestCase):
    def setUp(self):
        self.game = Game()
    
    def test_check_type(self):
        self.assertRaises(AssertionError, self.game.check, 'string')
    
    def test_check_correct(self):
        self.assertEqual(self.game.check(self.game.secret_number), 0, 'Should return 0')
    
    def test_check_over(self):
        self.assertEqual(self.game.check(self.game.secret_number + 1), 1, 'Should return 1')
    
    def test_check_under(self):
        self.assertEqual(self.game.check(self.game.secret_number - 1), -1, 'Should return -1')

if __name__ == '__main__':
    unittest.main()
