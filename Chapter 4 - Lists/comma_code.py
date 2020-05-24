# A program that takes a list and returns a string with all the items separated by a comma and a space,
# with "and" inserted before the last item


def list_to_string(inputList):
    if len(inputList) == 1:
        return inputList[0]

    combinedString = ''
    for i in range(len(inputList)):
        if i == (len(inputList) - 1) and len(inputList) > 1:
            combinedString += "and " + str(inputList[i])
        else:
            combinedString += str(inputList[i]) + ', '

    return combinedString


if __name__ == '__main__':
    print(list_to_string([]))
    print(list_to_string(['one']))
    print(list_to_string(['one', 'two', 'three']))
    print(list_to_string([1]))
    print(list_to_string([1, 2, 3]))
