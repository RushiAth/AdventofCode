handIn = open("input02.txt")

content = handIn.readlines()

for index in range(len(content)):
    content[index] = content[index].strip()
    content[index] = content[index].split()
    content[index][1] = int(content[index][1])

#problem 1

depth = 0
horizontal = 0

for line in content:
    if line[0] == 'forward':
        horizontal += line[1]
    elif line[0] == 'down':
        depth += line[1]
    else:
        depth -= line[1]

print(horizontal*depth)


#problem 2

depth = 0
aim = 0
horizontal = 0

for line in content:
    if line[0] == 'forward':
        horizontal += line[1]
        depth += aim*line[1]
    elif line[0] == 'down':
        aim += line[1]
    else:
        aim -= line[1]

print(horizontal*depth)