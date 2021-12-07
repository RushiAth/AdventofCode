import re

handIn = open('input2020_2.txt')

content = [line.strip() for line in handIn.readlines()]

policyPass = {}

for index in range(len(content)):
    line = content[index].split(': ')
    password = line[1]
    policyNum = line[0].split()[0]
    policyLetter = line[0].split()[1]

    
    
    