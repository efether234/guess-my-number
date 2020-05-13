# Guess My Number

This is a simple number guessing game—the computer chooses a random number, and the user tries to guess it.

## Playing the Game

```bash
$ git clone 'https://github.com/efether234/guess-my-number.git'
$ cd guess-my-number
$ python guessmynumber
```

From there, the game is self-explanatory (it's very simple.) You can quit at any time by typing `quit` into the prompt.

## The Game Class

This class contains the primary logic for running the game. The class `Game()` takes one parameter: difficulty. This *must* be one of the following (case-insensitive) strings: "Easy", "Medium", "Hard", or "Insane".

During initialization, the Game sets an `upper_bound` based on the input difficulty (and will throw a ValueError if it doesn't recognize the argument.) Then it chooses a random number between 1 and the `upper_bound` as the `secret_number`.

The only public method in the Game class is `check(guess)`. This takes an `int` and returns `1` if the `int` is greater than, `-1` if it is less than, and `0` if it is equal to the secret number:

```python
>>> from guessmynumber.game import Game
>>> game = Game('easy')
>>> game.secret_number
5
>>> game.check(6)
1
>>> game.check(4)
-1
>>> game.check(5)
0
```
