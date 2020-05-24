# A program that performs a simulation to calculate the probability that there is a streak
# of six heads or tails in a row within 100 random coin flips


import random


def simulate_streak_probability():
    numberOfStreaks = 0
    for experimentNumber in range(10000):
        # Code that creates a list of 100 'heads' or 'tails' values.
        flipResults = ''
        for flipNumber in range(100):
            randomNumber = random.randint(0, 1)
            if randomNumber == 0:
                flipResults += 'T'
            else:
                flipResults += 'H'

        # Code that checks if there is a streak of 6 heads or tails in a row.
        if ('TTTTTT' in flipResults) or ('HHHHHH' in flipResults):
            numberOfStreaks += 1
    print('Chance of streak: %s%%' % (numberOfStreaks / 100))


if __name__ == '__main__':
    simulate_streak_probability()
