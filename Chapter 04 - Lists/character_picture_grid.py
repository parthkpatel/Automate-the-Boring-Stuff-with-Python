# A program that takes a grid and prints out the values for the grid as if it were rotated 90 degrees clockwise


def print_grid(input_grid):
    num_rows = len(input_grid)
    num_columns = len(input_grid[0])

    for column in range(num_columns):
        for row in range(num_rows):
            print(input_grid[row][column], end='')
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
