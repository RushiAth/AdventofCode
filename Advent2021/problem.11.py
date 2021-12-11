handIn = open('testingInput.txt')
content = [[11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11]]

for i in range(10): 
    line = (handIn.readline()).strip()
    content.append([int(num) for num in line])
    
def step(lst):
    for index in range(1, len(lst)-1):
        for index2 in range(1, len(lst[index])-1):
            lst[index][index2] += 1
    
    return lst

def checkFlash(lst):
    for index in range(len(lst)):
        for index2 in range(len(lst[index])):
            if lst[index][index2] == 10:
                return True
    return False

def flash(lst):
    flashed = []
    done = []

    while checkFlash(lst) == True:
        for index in range(1, len(lst)-1):
            for index2 in range(1, len(lst[index])-1):
                if lst[index][index2] == 10 and (index, index2) not in done:
                    flashed.append(lst[index][index2])
                    lst[index][index2] = 0
                    done.append((index, index2))

                    lst[index-1][index2-1] += 1
                    lst[index-1][index2] += 1
                    lst[index-1][index2+1] += 1
                    lst[index][index2-1] += 1
                    lst[index][index2+1] += 1
                    lst[index+1][index2-1] += 1
                    lst[index+1][index2] += 1
                    lst[index+1][index2+1] += 1

    return lst, len(flashed)

for index in range(1, len(content)):
    content[index].insert(0, 11)
    content[index].append(11)
content.append([11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11])

sumFlash = 0

for i in range(10):
    content = step(content)
    #for i in content: print(i)
    returning = flash(content)
    sumFlash += returning[1]
    content = returning[0]
    #for i in content: print(i)
    #print()

print(sumFlash)