# A simple coin toss guessing game, where the user has two attempts to correctly guess the result of a flip

import random, pyinputplus as pyip


def coin_toss_game():
    guess_to_toss_dict = {0: 'tails', 1: 'heads'}
    coin_flip_guess_prompt = "Guess the coin toss! Enter 'heads' or 'tails':\n"
    guess = pyip.inputChoice(prompt=coin_flip_guess_prompt, choices=['heads', 'tails'])

    toss = random.randint(0, 1)  # 0 is tails, 1 is heads

    if guess_to_toss_dict[toss] == guess:
        print('You got it!')
    else:
        print('Nope! Guess again!')
        guess = pyip.inputChoice(prompt=coin_flip_guess_prompt, choices=['heads', 'tails'])
        if guess_to_toss_dict[toss] == guess:
            print('You got it!')
        else:
            print('Nope. You are really bad at this game.')


if __name__ == '__main__':
    coin_toss_game()
