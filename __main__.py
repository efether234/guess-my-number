"""A number guessing game.

The computer generates a random, secret integer and the user tries to guess
what the number is. The computer keeps track of the number of guesses from
the user."""

from game import Game

def setup(game):
    """Sets up the current game.

    Asks the user for a difficulty level, then sets the upper bound
    and generates the secret number."""

    while game.game_over:
        print("Please choose a difficulty level: Easy, Medium, Hard, or Insane")
        try:
            difficulty = input('Difficulty: ').lower()
            game.set_upper_bound(difficulty)
        except ValueError:
            print("Oops, that wasn't a valid response.\n")
            continue
        game.generate_secret_number()
        game.game_over = False

def play_again(game):
    """Asks the user if they want to play again.

    Takes input of either 'y' or 'n', then either resets the game
    or returns False to exit the program."""

    again = None
    while not again:
        again = input('Would you like to play again? (y/n) ')
        if again not in ('y', 'n'):
            again = None
    if again == 'y':
        game.game_over = True
        game.guesses = 0
        return True
    else:
        return False

def main():
    """Run the guess-my-number game."""

    game = Game()

    while True:
        setup(game)

        # Ask the user for a guess. If they enter something other than an int,
        # tell them and ask again.
        if game.guesses == 0:
            print("I'm thinking of a number between 1 and " + str(game.upper_bound) + ". \n")
        else:
            print('Number of guesses so far: ' + str(game.guesses))
        try:
            guess = int(input('Guess the number: '))
            game.guesses += 1
        except ValueError:
            print('Oops, try entering a number. \n')
            continue

        # Game.check() will return 1 if the guess is too high, -1 if the guess
        # is too low, and 0 if the guess is correct.
        if game.check(guess) == 1:
            print('That guess is too high. \n')
            continue
        if game.check(guess) == -1:
            print('That guess is too low. \n')
            continue
        if game.check(guess) == 0:
            print('Correct! It took you ' + str(game.guesses) + ' guesses! \n')

            # Ask the user if they would like to play again
            if not play_again(game):
                break

if __name__ == '__main__':
    main()
