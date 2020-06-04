# A program that takes a list and returns a string with all the items separated by a comma and a space,
# with "and" inserted before the last item


def list_to_string(input_list):
    if len(input_list) == 1:
        return input_list[0]

    combined_string = ''
    for i in range(len(input_list)):
        if i == (len(input_list) - 1) and len(input_list) > 1:
            combined_string += "and " + str(input_list[i])
        else:
            combined_string += str(input_list[i]) + ', '

    return combined_string


if __name__ == '__main__':
    print(list_to_string([]))
    print(list_to_string(['one']))
    print(list_to_string(['one', 'two', 'three']))
    print(list_to_string([1]))
    print(list_to_string([1, 2, 3]))
