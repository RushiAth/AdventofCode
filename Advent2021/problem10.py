handIn = open('input10.txt')
content = [line.strip() for line in handIn.readlines()]

errors = {')': 3, ']': 57, '}': 1197, '>': 25137}
scores = {')': 1, ']': 2, '}': 3, '>': 4}
brackets = {'(': ')', '[': ']', '{': '}', '<': '>'}
        
sumError = counter = 0
indexOfCorrupt = []
listOfEndings = []
listScores = []

for line in content:
    ending = []

    for char in line:
        if char in '([{<':
            ending.append(brackets[char])
        elif char == ')' and ending[-1] == ')':
            ending.pop()
        elif char == ']' and ending[-1] == ']':
            ending.pop()
        elif char == '}' and ending[-1] == '}':
            ending.pop()
        elif char == '>' and ending[-1] == '>': 
            ending.pop()
        else:
            sumError += errors[char]
            indexOfCorrupt.append(counter)
            break
    listOfEndings.append(ending)
    counter += 1

for index in range(len(listOfEndings)): 
    if index not in indexOfCorrupt:
        totalScore = 0
        for bracket in range(len(listOfEndings[index])-1, -1, -1):
            totalScore *= 5
            totalScore += scores[listOfEndings[index][bracket]]
        listScores.append(totalScore)

print('Part 1:', sumError)
print('Part 2:', sorted(listScores)[len(listScores)//2])