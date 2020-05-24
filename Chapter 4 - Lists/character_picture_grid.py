# A program that takes a grid and prints out the values for the grid as if it were rotated 90 degrees clockwise


def print_grid(inputGrid):
    numRows = len(inputGrid)
    numColumns = len(inputGrid[0])

    for column in range(numColumns):
        for row in range(numRows):
            print(inputGrid[row][column], end='')
        print()


if __name__ == '__main__':
    grid = [['.', '.', '.', '.', '.', '.'],
            ['.', 'O', 'O', '.', '.', '.'],
            ['O', 'O', 'O', 'O', '.', '.'],
            ['O', 'O', 'O', 'O', 'O', '.'],
            ['.', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', '.'],
            ['O', 'O', 'O', 'O', '.', '.'],
            ['.', 'O', 'O', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.']]

    print_grid(grid)
