from enum import Enum

class Direction(Enum):
    NE = 2
    SE = 4
    SW = 6
    NW = 8

grid = []
xmas_count = 0

def search_for_xmas(direction, row, column, desired_letter):
    if direction == Direction.NE:
        if row - 1 >= 0 and column + 1 < len(grid[row]) and grid[row - 1][column + 1] == desired_letter:
            return True
    elif direction == Direction.SE:
        if row + 1 < len(grid) and column + 1 < len(grid[row]) and grid[row + 1][column + 1] == desired_letter:
            return True
    elif direction == Direction.SW:
        if row + 1 < len(grid) and column - 1 >= 0 and grid[row + 1][column - 1] == desired_letter:
            return True
    elif direction == Direction.NW:
        if row - 1 >= 0 and column - 1 >= 0 and grid[row - 1][column - 1] == desired_letter:
            return True

    return False


for line in open('input.txt'):
    grid.append(list(line.strip()))

for rowi, row in enumerate(grid):
    for columni, column in enumerate(row):
        if column == 'A':
            if any([
                all([
                    search_for_xmas(Direction.NE, rowi, columni, 'S'),
                    search_for_xmas(Direction.SE, rowi, columni, 'S'),
                    search_for_xmas(Direction.SW, rowi, columni, 'M'),
                    search_for_xmas(Direction.NW, rowi, columni, 'M')
                ]),
                all([
                    search_for_xmas(Direction.NE, rowi, columni, 'M'),
                    search_for_xmas(Direction.SE, rowi, columni, 'S'),
                    search_for_xmas(Direction.SW, rowi, columni, 'S'),
                    search_for_xmas(Direction.NW, rowi, columni, 'M')
                ]),
                all([
                    search_for_xmas(Direction.NE, rowi, columni, 'M'),
                    search_for_xmas(Direction.SE, rowi, columni, 'M'),
                    search_for_xmas(Direction.SW, rowi, columni, 'S'),
                    search_for_xmas(Direction.NW, rowi, columni, 'S')
                ]),
                all([
                    search_for_xmas(Direction.NE, rowi, columni, 'S'),
                    search_for_xmas(Direction.SE, rowi, columni, 'M'),
                    search_for_xmas(Direction.SW, rowi, columni, 'M'),
                    search_for_xmas(Direction.NW, rowi, columni, 'S')
                ])
            ]):
                xmas_count += 1


print(xmas_count)
