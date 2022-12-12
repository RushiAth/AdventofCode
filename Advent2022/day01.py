handIn = open('input01.txt')

elves = (handIn.read()).split('\n\n')
food = []

for i in range(len(elves)):
    elf = list(map(int, elves[i].split()))

    food.append(sum(elf))

#Part 1
print(max(food))

#Part 2
food.sort()

print(sum(food[-3:]))