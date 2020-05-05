"""
A module that contains the logic for playing the game.

Classes
-------
    Game
        A class that represents an instance of the number-guessing game.
"""
import random


class Game:
    """
    A class that represents an instance of the number-guessing game.

    Attributes
    ----------
    game_over : bool
        whether the game has ended
    upper_bound : int
        the upper limit of the secret number
    secret_number : int
        the number the user is trying to guess

    Methods
    -------
    set_upper_bound(difficulty)
        Set the game's upper bound based on a user selected difficulty.
    check(guess)
        Check to see if user's guess is correct

    """

    def __init__(self):
        self.game_over = True
        self.upper_bound = None
        self.secret_number = None

    def __repr__(self):
        return "<Game - Upper bound: " + str(self.upper_bound) + \
            ", Secret number: " + str(self.secret_number) + ">"

    def __set_secret_number(self):
        if self.upper_bound:
            self.secret_number = random.randint(1, self.upper_bound)
        else:
            self.secret_number = random.randint(1, 10)

    def set_upper_bound(self, difficulty):
        """
        Set the game's upper bound based on a user selected difficulty.

        Parameters
        ----------
        difficulty : str
            The user selected difficulty for the game.

        Raises
        ------
        ValueError
            If user entered difficulty is not in list of expected
            values.
        """

        # Check that user entered valid request.
        if difficulty not in ('easy', 'medium', 'hard', 'insane'):
            raise ValueError(
                "Choice must be either 'easy', 'medium', 'hard', or 'insane'")

        # Set upper bound based on what user entered.
        if difficulty == 'easy':
            self.upper_bound = 10
        elif difficulty == 'medium':
            self.upper_bound = 20
        elif difficulty == 'hard':
            self.upper_bound = 100
        else:
            self.upper_bound = 1000

        # Set the game's secret number
        self.__set_secret_number()

    def check(self, guess):
        """
        Check to see if user's guess is correct.

        Parameters
        ----------
            guess : int
                The user's guess.
        Returns
        -------
            int
                1 if the user's guess is too high, -1 if the user's
                guess is too low, 0 if the user's guess is correct.
        """

        assert isinstance(guess, int), "Input should be of type Int"

        if guess > self.secret_number:
            return 1
        elif guess < self.secret_number:
            return -1
        # If guess is not too big or too small, it must be correct
        else:
            return 0
