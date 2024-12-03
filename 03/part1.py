import re

pattern = re.compile(r'mul\((\d*),(\d*)\)')

program_sum = 0

for line in open('input.txt'):
    matches = re.findall(pattern, line)
    if matches:
        line_sum = sum([int(left) * int(right) for left, right in matches])
        program_sum += line_sum

print(program_sum)
