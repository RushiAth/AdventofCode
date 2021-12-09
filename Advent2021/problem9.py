handIn = open('input9.txt')
content = [line.strip() for line in handIn.readlines()]

def checkS(num, index1, index2, lst):
    surrounding = [lst[index1-1][index2], lst[index1][index2-1], lst[index1][index2+1], lst[index1+1][index2]]

    tf = [num < SNum for SNum in surrounding]

    return all(tf) 

for index in range(len(content)):
    content[index] = '9' + content[index] + '9'

content.insert(0, '9'*len(content[0]))
content.append('9'*len(content[0]))

risk = 0

for index in range(1, len(content)-1):
    for index2 in range(1, len(content[index])-1):
        if checkS(content[index][index2], index, index2, content) == True:
            risk += (int(content[index][index2]) + 1)

print(risk)