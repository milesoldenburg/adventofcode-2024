import re

pattern = re.compile(r'mul\((\d*),(\d*)\)')
do_pattern = re.compile(r"(^|do\(\))(.+?)(don't\(\)|$)")

program_sum = 0

for line in open('input.txt'):
    matches = re.findall(do_pattern, line)
    if matches:
        for line_match in matches:
            line_matches = re.findall(pattern, line_match[1])
            if line_matches:
                line_sum = sum([int(left) * int(right) for left, right in line_matches])
                program_sum += line_sum

print(program_sum)
