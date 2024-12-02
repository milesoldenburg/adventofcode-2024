from enum import Enum
from itertools import pairwise


class Direction(Enum):
    ASCENDING = 1
    DESCENDING = 2


def is_report_safe(levels):
    safe = True
    d = None

    if levels[0] < levels[1]:
        d = Direction.ASCENDING
    elif levels[0] > levels[1]:
        d = Direction.DESCENDING
    else:
        return False

    for left, right in pairwise(levels):
        if left == right or (d == Direction.ASCENDING and left > right) or (d == Direction.DESCENDING and left < right) or abs(left - right) > 3:
            safe = False
            break
    return safe

safe_reports = 0

for line in open('input.txt'):
    levels = [int(x) for x in line.split()]

    if is_report_safe(levels):
        safe_reports += 1
    else:
        for i, level in enumerate(levels):
            levels_copy = levels.copy()
            levels_copy.pop(i)
            if is_report_safe(levels_copy):
                safe_reports += 1
                break

print(safe_reports)
