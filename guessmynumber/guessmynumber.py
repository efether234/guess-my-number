"""
A module that contains the logic for playing the game.
"""
import random


class Game:
    """
    A class that represents an instance of the number-guessing game.

    Attributes
    ----------
    game_over : bool
        Whether the game has ended.
    upper_bound : int
        The upper limit of the secret number,
    secret_number : int
        The number the user is trying to guess,

    Methods
    -------
    set_upper_bound(difficulty)
        Set the game's upper bound based on a user selected difficulty.
    check(guess)
        Check to see if user's guess is correct

    """

    def __init__(self, difficulty):
        """
        Parameters
        ----------
        difficulty : str
            User selected difficulty.
        """

        self.game_over = False
        self.upper_bound = self._set_upper_bound(difficulty)
        self.secret_number = self._set_secret_number(self.upper_bound)

    def __repr__(self):
        return "<Game - Upper bound: " + str(self.upper_bound) + \
            ", Secret number: " + str(self.secret_number) + ">"

    def _set_secret_number(self, upper_bound):
        # Return a secret number between 1 and the upper bound.
        return random.randint(1, upper_bound)

    def _set_upper_bound(self, difficulty):
        # Return an upper bound based on the difficulty selected by user.

        # Check that user entered valid request.
        if difficulty not in ('easy', 'medium', 'hard', 'insane'):
            raise ValueError(
                "Choice must be either 'easy', 'medium', 'hard', or 'insane'")

        # Set upper bound based on what user entered.
        if difficulty == 'easy':
            return 10
        elif difficulty == 'medium':
            return 20
        elif difficulty == 'hard':
            return 100
        else:
            return 1000

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
