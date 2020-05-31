# A program that takes a list of strings and displays it in
# a well-organized table with each column right-justified.


def print_table(table):
    colWidths = get_col_widths(table)
    for column in range(len(table[0])):
        for row in range(len(table)):
            print(table[row][column].rjust(colWidths[row]), end=' ')
        print()


def get_col_widths(table):
    colWidths = [0] * len(table)
    count = 0
    while count < len(table):
        for item in table[count]:
            if len(item) > colWidths[count]:
                colWidths[count] = len(item)
        count += 1

    return colWidths


if __name__ == '__main__':
    tableData = [['apples', 'oranges', 'cherries', 'banana'],
                 ['Alice', 'Bob', 'Carol', 'David'],
                 ['dogs', 'cats', 'moose', 'goose']]
    print_table(tableData)
