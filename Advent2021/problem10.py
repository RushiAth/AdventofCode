handIn = open('input10.txt')
content = [line.strip() for line in handIn.readlines()]

def checkError(character):
    if character == ')':
        return 3
    elif character == ']':
        return 57
    elif character == '}':
        return 1197
    else:
        return 25137

def checkScore(character):
    if character == ')':
        return 1
    elif character == ']':
        return 2
    elif character == '}':
        return 3
    else:
        return 4
        
sumError = 0
counter = 0
indexOfCorrupt = []
listOfEndings = []

for line in content:
    ending = []

    for char in line:
        if char == '(':
            ending.append(')')
        elif char == '[':
            ending.append(']')
        elif char == '{':
            ending.append('}')
        elif char == '<':
            ending.append('>')
        elif char == ')' and ending[-1] == ')':
            ending.pop()
        elif char == ']' and ending[-1] == ']':
            ending.pop()
        elif char == '}' and ending[-1] == '}':
            ending.pop()
        elif char == '>' and ending[-1] == '>': 
            ending.pop()
        else:
            sumError += checkError(char)
            indexOfCorrupt.append(counter)
            break
    listOfEndings.append(ending)
    counter += 1

print('Part 1:', sumError)


listScores = []

for index in range(len(listOfEndings)): 
    if index not in indexOfCorrupt:
        totalScore = 0
        for bracket in range(len(listOfEndings[index])-1, -1, -1):
            totalScore *= 5
            totalScore += checkScore(listOfEndings[index][bracket])
        listScores.append(totalScore)

print('Part 2:', sorted(listScores)[len(listScores)//2])