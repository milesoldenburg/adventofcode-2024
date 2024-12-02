from enum import Enum
from itertools import pairwise


class Direction(Enum):
    ASCENDING = 1
    DESCENDING = 2

safe_reports = 0

for line in open('input.txt'):
    levels = [int(x) for x in line.split()]

    d = None

    if levels[0] < levels[1]:
        d = Direction.ASCENDING
    elif levels[0] > levels[1]:
        d = Direction.DESCENDING
    else:
        continue

    any_failure = False
    for left, right in pairwise(levels):
        if left == right or (d == Direction.ASCENDING and left > right) or (d == Direction.DESCENDING and left < right) or abs(left - right) > 3:
            any_failure = True
            break

    if not any_failure:
        safe_reports += 1

print(safe_reports)
