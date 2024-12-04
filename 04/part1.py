from enum import Enum

class Direction(Enum):
    N = 1
    NE = 2
    E = 3
    SE = 4
    S = 5
    SW = 6
    W = 7
    NW = 8

grid = []
xmas_count = 0

def search_for_xmas(direction, row, column):
    desired_letter = None
    if grid[row][column] == 'X':
        desired_letter = 'M'
    elif grid[row][column] == 'M':
        desired_letter = 'A'
    elif grid[row][column] == 'A':
        desired_letter = 'S'
    elif grid[row][column] == 'S':
        return True

    if direction == Direction.N:
        if row - 1 >= 0 and grid[row - 1][column] == desired_letter:
            return search_for_xmas(direction, row - 1, column)
    elif direction == Direction.NE:
        if row - 1 >= 0 and column + 1 < len(grid[row]) and grid[row - 1][column + 1] == desired_letter:
            return search_for_xmas(direction, row - 1, column + 1)
    elif direction == Direction.E:
        if column + 1 < len(grid[row]) and grid[row][column + 1] == desired_letter:
            return search_for_xmas(direction, row, column + 1)
    elif direction == Direction.SE:
        if row + 1 < len(grid) and column + 1 < len(grid[row]) and grid[row + 1][column + 1] == desired_letter:
            return search_for_xmas(direction, row + 1, column + 1)
    elif direction == Direction.S:
        if row + 1 < len(grid) and grid[row + 1][column] == desired_letter:
            return search_for_xmas(direction, row + 1, column)
    elif direction == Direction.SW:
        if row + 1 < len(grid) and column - 1 >= 0 and grid[row + 1][column - 1] == desired_letter:
            return search_for_xmas(direction, row + 1, column - 1)
    elif direction == Direction.W:
        if column - 1 >= 0 and grid[row][column - 1] == desired_letter:
            return search_for_xmas(direction, row, column - 1)
    elif direction == Direction.NW:
        if row - 1 >= 0 and column - 1 >= 0 and grid[row - 1][column - 1] == desired_letter:
            return search_for_xmas(direction, row - 1, column - 1)

    return False


for line in open('input.txt'):
    grid.append(list(line.strip()))

for rowi, row in enumerate(grid):
    for columni, column in enumerate(row):
        if column == 'X':
            for d in Direction:
                if search_for_xmas(d, rowi, columni):
                    xmas_count += 1

print(xmas_count)
