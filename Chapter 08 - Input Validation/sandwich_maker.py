# Program that that asks users for their sandwich preferences using the PyInputPlus module
# The program will then print out these preferences in a summary table

import pyinputplus as pyip


def take_sandwich_order():
    sandwich_items = []

    print('What type of bread would you like?')
    sandwich_items.append(pyip.inputMenu(['Wheat', 'White', 'Sourdough'], numbered=True))

    print('Which protein would you like on your sandwich?')
    sandwich_items.append(pyip.inputMenu(['Chicken', 'Turkey', 'Ham', 'Tofu'], numbered=True))

    if pyip.inputYesNo('Would you like cheese on your sandwich?\n') == 'yes':
        print('Which type of cheese would you like on your sandwich?')
        sandwich_items.append(pyip.inputMenu(['Cheddar', 'Swiss', 'Mozzarella'], numbered=True))

    # Ask user if they want any of the additional toppings
    additional_toppings = ['Mayo', 'Mustard', 'Lettuce', 'Tomato']
    for topping in additional_toppings:
        prompt_additional_topping = 'Would you like %s on your sandwich?\n' % topping
        if pyip.inputYesNo(prompt_additional_topping) == 'yes':
            sandwich_items.append(topping)

    prompt_num_of_sandwiches = 'How many sandwiches would you like?\n'
    number_of_sandwiches = pyip.inputInt(prompt_num_of_sandwiches, min=1)

    summarize_sandwich_order(sandwich_items, number_of_sandwiches)


def summarize_sandwich_order(sandwich_items, number_of_sandwiches):
    sandwich_items_and_prices = {'Wheat': 1.5, 'White': 1.25, 'Sourdough': 1.25,
                                 'Chicken': 2.0, 'Turkey': 2.25, 'Ham': 2.5, 'Tofu': 1.5,
                                 'Cheddar': 1.0, 'Swiss': 1.0, 'Mozzarella': 1.25,
                                 'Mayo': 0.25, 'Mustard': 0.2, 'Lettuce': 0.1, 'Tomato': 0.25}

    # Print out a summary table of the sandwich items, their price, and the total price of the sandwich
    print('SANDWICH ORDER SUMMARY'.center(30, '-'))
    total_price = 0
    for item in sandwich_items:
        print(item.ljust(20), sandwich_items_and_prices[item], sep=": ")
        total_price += sandwich_items_and_prices[item]
    print(''.center(30, '-'))
    print(''.ljust(21), str(total_price))
    print(''.ljust(21), 'x' + str(number_of_sandwiches))
    total_price = round(total_price * number_of_sandwiches, 2)
    print(''.center(30, '-'))
    print('TOTAL PRICE'.ljust(20), total_price, sep=": ")


if __name__ == '__main__':
    take_sandwich_order()
