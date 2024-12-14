ordering_rules = []
updates = []

for line in open('input.txt'):
    if '|' in line:
        left, right = line.strip().split('|')
        ordering_rules.append((left, right))
    elif ',' in line:
        updates.append(line.strip().split(','))

sum_middle_pages = 0

for update in updates:
    correctly_ordered = True

    for rule in ordering_rules:
        left, right = rule

        if left in update and right in update:
            if update.index(left) > update.index(right):
                correctly_ordered = False
                break

    if correctly_ordered:
        sum_middle_pages += int(update[len(update) // 2])

print(sum_middle_pages)
