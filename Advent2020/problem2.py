import re

handIn = open('input2020_2.txt')

content = [line.strip() for line in handIn.readlines()]
print(len(content))
counter = 0

for index in range(len(content)):
    line = content[index].split(': ')
    password = line[1]
    policyNums = line[0].split()[0].split('-')
    policyLetter = line[0].split()[1]

    letterInPass = password.count(policyLetter)

    if int(policyNums[0]) <= letterInPass <= int(policyNums[1]):
        counter += 1

print(counter)
    