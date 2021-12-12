handIn = open('input11.txt')
content = [[11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11]]

for i in range(10): 
    content.append([int(num) for num in (handIn.readline()).strip()])
    content[i+1].insert(0, 11)
    content[i+1].append(11)
content.append([11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11])

def checkFlash(lst):
    for index in range(1, len(lst)-1):
        for index2 in range(1, len(lst[index])-1):
            if lst[index][index2] >= 10:
                return True
    return False

def flash(lst):
    done = []
    
    for index in range(1, len(lst)-1):
        for index2 in range(1, len(lst[index])-1):
            lst[index][index2] += 1

    while checkFlash(lst) == True:
        for index in range(1, len(lst)-1):
            for index2 in range(1, len(lst[index])-1):
                if lst[index][index2] >= 10 and (index, index2) not in done:
                    lst[index][index2] = 0
                    done.append((index, index2))

                    if (index-1, index2-1) not in done:
                        lst[index-1][index2-1] += 1
                    if (index-1, index2) not in done:
                        lst[index-1][index2] += 1
                    if (index-1, index2+1) not in done:
                        lst[index-1][index2+1] += 1
                    if (index, index2-1) not in done:
                        lst[index][index2-1] += 1
                    if (index, index2+1) not in done:
                        lst[index][index2+1] += 1
                    if (index+1, index2-1) not in done:
                        lst[index+1][index2-1] += 1
                    if (index+1, index2) not in done:
                        lst[index+1][index2] += 1
                    if (index+1, index2+1) not in done:
                        lst[index+1][index2+1] += 1

    return lst, len(done)

def checkAllFlash(lst):
    for index in range(1, len(lst)-1):
        for index2 in range(1, len(lst[index])-1):
            if lst[index][index2] != 0:
                return False
    return True

sumFlash = 0
stepValue = 0

while checkAllFlash(content) == False:
    stepValue += 1
    returning = flash(content)

    if stepValue <= 100:
        sumFlash += returning[1]
    content = returning[0]

print('Part 1:', sumFlash)
print('Part 2:', stepValue)