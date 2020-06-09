# A program that performs a simulation to calculate the probability that there is a streak
# of six heads or tails in a row within 100 random coin flips


import random


def simulate_streak_probability():
    number_of_streaks = 0
    for experimentNumber in range(10000):
        # Code that creates a list of 100 'heads' or 'tails' values.
        flip_results = ''
        for i in range(100):
            random_number = random.randint(0, 1)
            if random_number == 0:
                flip_results += 'T'
            else:
                flip_results += 'H'

        # Code that checks if there is a streak of 6 heads or tails in a row.
        if ('TTTTTT' in flip_results) or ('HHHHHH' in flip_results):
            number_of_streaks += 1
    print('Chance of streak: %s%%' % (number_of_streaks / 100))


if __name__ == '__main__':
    simulate_streak_probability()
