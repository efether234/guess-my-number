from guess_my_number import Game

def main():
    game = Game()
    print("I'm thinking of a number between 1 and " + str(game.upper_bound) + ".")
    while True:
        try:
            guess = int(input('Guess the number: '))
        except ValueError:
            print('Oops, try entering a number.')
            continue
        if game.check(guess) == 1:
            print('That guess is too high.')
            continue
        if game.check(guess) == -1:
            print('That guess is too low.')
            continue
        print('Correct!')
        return False

if __name__ == '__main__':
    main()