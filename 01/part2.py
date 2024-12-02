from collections import Counter

lefts = []
rights = []

for line in open('input.txt'):
    left, right = line.split()
    lefts.append(left)
    rights.append(right)

rights = Counter(rights)

similarity_score = 0
for left in lefts:
    similarity_score += int(left) * rights[left]

print(similarity_score)
