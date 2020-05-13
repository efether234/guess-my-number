from cmd import Cmd
from game import Game


class App(Cmd):
    game = None
    prompt = 'Guess: '

    def preloop(self):
        print('Please select a difficulty: Easy, Medium, Hard, Insane')
        while not self.game:
            difficulty = input('Difficulty: ')
            try:
                self.game = Game(difficulty)
                print("I'm thinking of a number between 1 and {}.".format(
                    self.game.upper_bound))
            except ValueError:
                self.default(difficulty)

    def postloop(self):
        print('Thanks for playing!')

    def precmd(self, line):
        try:
            # If line can be cast as an int, append "guess " to the
            # front. (Must be cast back to a str for the do_guess()
            # method to work.)
            return 'guess ' + str(int(line))
        except:
            return line

    def do_guess(self, line):
        result = self.game.check(int(line))
        if result > 0:
            print("That's too high.")
        elif result < 0:
            print("That's too low.")
        else:
            print("That's right!")
            return True

    def do_quit(self, line):
        return True

    def default(self, line):
        print("Oops, try that again.")
