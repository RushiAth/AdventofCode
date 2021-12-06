from collections import Counter

handIn = open('input5.txt')
content = handIn.readlines()

for index in range(len(content)):
    content[index] = content[index].split(' -> ')
    content[index][0], content[index][1] = content[index][0].split(','), (content[index][1].strip('\n')).split(',')
    content[index][0], content[index][1] = (int(content[index][0][0]), int(content[index][0][1])), (int(content[index][1][0]), int(content[index][1][1]))

allCoords = []

for line in content:
    minX, maxX = min([line[0][0], line[1][0]]), max([line[0][0], line[1][0]])
    minY, maxY = min([line[0][1], line[1][1]]), max([line[0][1], line[1][1]])
    
    if line[0][0] == line[1][0]:
        for num in range(minY, maxY+1):
            allCoords.append((line[0][0], num))
    elif line[0][1] == line[1][1]:
        for num in range(minX, maxX+1):
            allCoords.append((num, line[1][1]))
    else:
        if line[0][0] > line[1][0]:
            if line[0][1] > line[1][1]:
                for i in range(maxX-minX+1):
                    allCoords.append((line[0][0]-i,line[0][1]-i))
            else:
                for i in range(maxX-minX+1):
                    allCoords.append((line[0][0]-i,line[0][1]+i))
        else:
            if line[0][1] > line[1][1]:
                for i in range(maxX-minX+1):
                    allCoords.append((line[0][0]+i,line[0][1]-i))
            else:
                for i in range(maxX-minX+1):
                    allCoords.append((line[0][0]+i,line[0][1]+i))

counter = 0

for num in Counter(allCoords).values():
    if num >= 2:
        counter += 1

print(counter)