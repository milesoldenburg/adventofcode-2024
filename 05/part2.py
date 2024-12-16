ordering_rules = []
updates = []
incorrect_updates = []

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
                incorrect_updates.append(update)
                break

correct_updates = []
for update in incorrect_updates:
    correct_update = []
    for i, page in enumerate(update):
        prior_rules = filter(lambda rule: rule[0] == page, ordering_rules)
        prior_values = [rule[1] for rule in prior_rules]

        cu_indexes = []
        for prior_value in prior_values:
            if prior_value in correct_update:
                cu_indexes.append(correct_update.index(prior_value))

        if cu_indexes:
            correct_update.insert(min(cu_indexes), page)
        else:
            correct_update.append(page)

    sum_middle_pages += int(correct_update[len(correct_update) // 2])


print(sum_middle_pages)
