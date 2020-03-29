from random import random
from math import ceil

class Game:
    """A game object.

    Has attributes of upper bound and secret number. __generate_number()
    generates a random number between 1 and the upper_bound inclusive.
    User tries to guess the secret number."""
    def __init__(self):
        self.upper_bound = 20
        self.secret_number = self.__generate_number()

    def __repr__(self):
        return "<Game - Upper bound: " + str(self.upper_bound) + \
            ", Secret number: " + str(self.secret_number) + ">"

    def __generate_number(self):
        return ceil(random() * self.upper_bound)

    def check(self, guess):
        """Check to see if guess is correct.

        Accepts user's guess, then compares it to secret_number.
        If guess is correct, return zero. Otherwise, export 1 of -1
        if guess is too big or too small, respectively."""

        assert isinstance(guess, int), "Input should be of type Int"

        if guess > self.secret_number:
            return 1
        if guess < self.secret_number:
            return -1
        # If guess is not too big or too small, it must be correct
        return 0
