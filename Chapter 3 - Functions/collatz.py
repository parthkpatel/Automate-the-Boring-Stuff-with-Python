# A simple program that explores The Collatz Sequence


def collatz(input_number):
    if input_number % 2 == 0:
        print(input_number // 2)
        return input_number // 2
    elif input_number % 2 == 1:
        print(input_number * 3 + 1)
        return input_number * 3 + 1


if __name__ == '__main__':
    print("Enter an integer greater than 1:")
    try:
        number = int(input())
        if number > 1:
            while True:
                number = collatz(number)
                if number == 1:
                    break
        else:
            print("You did not choose an integer greater than 1. Exiting program.")
    except ValueError:
        print("Error: You must enter an integer. Exiting program.")
