from enum import Enum

class Direction(Enum):
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4

grid = []
start = None

for line in open('input.txt'):
    row = list(line.strip())
    if '^' in row:
        start = (row.index('^'), len(grid))
    grid.append([(obstacle, False) for obstacle in row])

x, y = start
direction = Direction.NORTH

while True:
    # Mark current location as visited
    grid[y][x] = (grid[y][x][0], True)

    if direction == Direction.NORTH:
        if y - 1 < 0:
            break
        elif grid[y - 1][x][0] == '#':
            direction = Direction.EAST
            if x + 1 >= len(grid[0]):
                break
            else:
                x += 1
        else:
            y -= 1
    elif direction == Direction.EAST:
        if x + 1 >= len(grid[0]):
            break
        elif grid[y][x + 1][0] == '#':
            direction = Direction.SOUTH
            if y + 1 >= len(grid):
                break
            else:
                y += 1
        else:
            x += 1
    elif direction == Direction.SOUTH:
        if y + 1 >= len(grid):
            break
        elif grid[y + 1][x][0] == '#':
            direction = Direction.WEST
            if x - 1 < 0:
                break
            else:
                x -= 1
        else:
            y += 1
    elif direction == Direction.WEST:
        if x - 1 < 0:
            break
        elif grid[y][x - 1][0] == '#':
            direction = Direction.NORTH
            if y - 1 < 0:
                break
            else:
                y -= 1
        else:
            x -= 1

visited_squares = 0
for row in grid:
    for column in row:
        if column[1]:
            visited_squares += 1

print(visited_squares)
