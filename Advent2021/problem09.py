handIn = open('input09.txt')
content = [line.strip() for line in handIn.readlines()]

def checkSurrounding(num, index1, index2, lst):
    surrounding = [lst[index1-1][index2], lst[index1][index2-1], lst[index1][index2+1], lst[index1+1][index2]]
    tf = [num < SNum for SNum in surrounding]

    return all(tf)

def basinHelp(basinPosition, num, lst):
    y, x = basinPosition[0], basinPosition[1]
    tiles = {(y-1, x): int(lst[y-1][x]), (y, x-1): int(lst[y][x-1]), (y, x+1): int(lst[y][x+1]), (y+1, x): int(lst[y+1][x])}
    returning = {}

    for i in tiles:
        if tiles[i] >= int(num)+1 and tiles[i] != 9:
            returning.update({i: tiles[i]})
    return returning

def basin(basinPosition, num, lst):
    sizeCounter = {basinPosition: int(num)}
    basinContents = {basinPosition: int(num)}

    while len(basinContents) != 0:
        continuingBasin = basinHelp(list(basinContents.keys())[0], list(basinContents.values())[0], lst)
        basinContents.update(continuingBasin)
        sizeCounter.update(continuingBasin)
        basinContents.pop(list(basinContents.keys())[0])

    return len(sizeCounter)

for index in range(len(content)):
    content[index] = '9' + content[index] + '9'

content.insert(0, '9'*len(content[0]))
content.append('9'*len(content[0]))

#Part 1
risk = 0
basinCenters = {}

for index in range(1, len(content)-1):
    for index2 in range(1, len(content[index])-1):
        if checkSurrounding(content[index][index2], index, index2, content):
            basinCenters[(index, index2)] = content[index][index2]
            risk += (int(content[index][index2]) + 1)

print('Risk (Part 1):', risk)

#Part 2
basinSizes = []

for b in basinCenters:
    basinSizes.append(basin(b, basinCenters[b], content))

print('Basin Sizes:', sorted(basinSizes, reverse=True)[:3])