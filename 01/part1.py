lefts = []
rights = []

for line in open('input.txt'):
    left, right = line.split()
    lefts.append(int(left))
    rights.append(int(right))

lefts.sort()
rights.sort()

distance = 0
for i in range(0, len(lefts)):
    distance += abs(lefts[i] - rights[i])

print(distance)
