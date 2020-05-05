from .guessmynumber import Game


def main():
    game = Game()
    guesses = 0

    while True:
        while game.game_over:
            print("Please choose a difficulty level: "
                  "Easy, Medium, Hard, or Insane")
            try:
                difficulty = input('Difficulty: ').lower()
                game.set_upper_bound(difficulty)
            except ValueError:
                print("Oops, that wasn't a valid response.\n")
                continue
            # game.set_secret_number()
            game.game_over = False

        # Ask the user for a guess. If they enter something other than
        # an int, tell them and ask again.
        if guesses == 0:
            print("I'm thinking of a number between 1 and " +
                  str(game.upper_bound) + ". \n")
        else:
            print('Number of guesses so far: ' + str(guesses))
        try:
            guess = int(input('Guess the number: '))
            guesses += 1
        except ValueError:
            print('Oops, try entering a number. \n')
            continue

        # Game.check() will return 1 if the guess is too high, -1 if the
        # guess is too low, and 0 if the guess is correct.
        if game.check(guess) == 1:
            print('That guess is too high. \n')
            continue
        if game.check(guess) == -1:
            print('That guess is too low. \n')
            continue
        if game.check(guess) == 0:
            print('Correct! It took you ' + str(guesses) + ' guesses! \n')

            # Ask the user if they would like to play again
            play_again = None
            while not play_again:
                play_again = input('Would you like to play again? (y/n) ')
                if play_again not in ('y', 'n'):
                    play_again = None
            if play_again == 'y':
                game.game_over = True
                guesses = 0
            else:
                break


if __name__ == '__main__':
    main()
