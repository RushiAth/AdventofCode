handIn = open('testingInput.txt')
content = [line.strip() for line in handIn.readlines()]

def checkSurrounding(num, index1, index2, lst):
    surrounding = [lst[index1-1][index2], lst[index1][index2-1], lst[index1][index2+1], lst[index1+1][index2]]
    tf = [num < SNum for SNum in surrounding]

    return all(tf) 

def basin(basins, lst):
    size = 0


    return size

for index in range(len(content)):
    content[index] = '9' + content[index] + '9'

content.insert(0, '9'*len(content[0]))
content.append('9'*len(content[0]))

#Part 1
risk = 0
basinCenters = {}

for index in range(1, len(content)-1):
    for index2 in range(1, len(content[index])-1):
        if checkSurrounding(content[index][index2], index, index2, content) == True:
            basinCenters[(index, index2)] = content[index][index2]
            risk += (int(content[index][index2]) + 1)

print(risk)

#Part 2
basinSizes = []
print(basinCenters)

for b in basinCenters:
    basinSizes.append(basin(basinCenters, content))

print(sorted(basinSizes))


# for i in content:
#     for j in i:
#         if j == '9':
#             print('\033[1;31;40mX', end='')
#         else:
#             print('\033[1;32;40m.', end='')
#     print()
# print('\033[0;37;40m')