def countTrees (right, down):
    trees = 0
    position = [0, 0]

    for index in range(len(lines)-1):
        position[0] += down
        position[1] += right

        if position[1] > 30:
            position[1] -= 31

        if position[0] > 323:
            break

        if lines[position[0]][position[1]] == '#':
            trees += 1

    return trees

handIn = open('input2020_3.txt')
lines = handIn.readlines()

#Part 1
print(countTrees(3, 1))

#Part 2
print(countTrees(1, 1) * countTrees(3, 1) * countTrees(5, 1) * countTrees(7, 1) * countTrees(1, 2))