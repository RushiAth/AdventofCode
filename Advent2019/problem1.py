handIn = open('Advent2019/input1.txt')

content = handIn.read()
content = content.split()

#problem 1

fuelList = []

for index in range(len(content)):
    content[index] = int(content[index])
    fuelList.append(content[index]//3 -2)

print(sum(fuelList))


#problem 2

fuelList = []

for index in range(len(content)):
    content[index] = int(content[index])
    moduleFuel = 0

    while True:   
        if (content[index]//3 - 2) > 0:
            moduleFuel += content[index]//3 - 2
        content[index] = content[index]//3 - 2

        if content[index] <= 0:
            break

    fuelList.append(moduleFuel)

print(sum(fuelList))