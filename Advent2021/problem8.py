def findNumSum(input, output):
    numSum = 0


    return numSum


handIn = open('input8.txt')

content = [(line.strip()).split(' | ') for line in (handIn.readlines())]
totalSum = 0

for index in range(len(content)):
    totalSum += findNumSum(content[index][0], content[index][1])


#part 1
'''
counter = 0
for index in range(len(content)):
    value = content[index][1].split()

    for i in value:
        if len(i) in [2, 3, 4, 7]:
            sum += 1

print(counter)
'''