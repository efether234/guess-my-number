from random import randint

class Game:
    """A game object.

    Has attributes of upper bound and secret number. __generate_number()
    generates a random number between 1 and the upper_bound inclusive.
    User tries to guess the secret number."""

    def __init__(self):
        self.game_over = True
        self.upper_bound = None
        self.secret_number = None

    def __repr__(self):
        return "<Game - Upper bound: " + str(self.upper_bound) + \
            ", Secret number: " + str(self.secret_number) + ">"

    def set_upper_bound(self, difficulty):
        """Set upper bound for the game.

        Takes difficulty specified by the user, then sets self.upper_bound
        to 10, 20, 100, or 1000 depending on the dificulty input."""

        # Check that user entered valid request.
        if difficulty not in ('easy', 'medium', 'hard', 'insane'):
            raise ValueError("Choice must be either 'easy', 'medium', 'hard', or 'insane'")

        # Set upper bound based on what user entered.
        if difficulty == 'easy':
            self.upper_bound = 10
        elif difficulty == 'medium':
            self.upper_bound = 20
        elif difficulty == 'hard':
            self.upper_bound = 100
        else:
            self.upper_bound = 1000


    def generate_secret_number(self):
        """Sets self.secret_number to a random inter between 1 and self.upper_bound inclusive."""
        if self.upper_bound:
            self.secret_number = randint(1, self.upper_bound)
        else:
            self.secret_number = randint(1, 10)

    def check(self, guess):
        """Check to see if guess is correct.

        Accepts user's guess, then compares it to secret_number.
        If guess is correct, return zero. Otherwise, export 1 of -1
        if guess is too big or too small, respectively."""

        assert isinstance(guess, int), "Input should be of type Int"

        if guess > self.secret_number:
            return 1
        elif guess < self.secret_number:
            return -1
        # If guess is not too big or too small, it must be correct
        else:
            return 0
