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
        
ending = []
sumError = 0

for line in content:
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
            break

print(sumError)