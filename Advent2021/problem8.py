handIn = open('testingInput.txt')
content = [(line.strip()).split(' | ') for line in (handIn.readlines())]

#part 1
counter = 0

for index in range(len(content)):
    value = content[index][1].split()

    for i in value:
        if len(i) in [2, 3, 4, 7]:
            sum += 1

print(counter)


#part 2
def mappingNum(input):
    mapping = {'top': '', 'middle': '', 'bottom': '', 'topright': '', 'topleft': '', 'bottomright': '', 'bottomleft': ''}

    input = sorted(input.split())
    print(input)

    for letters in input:
        if len(letters) == 2:
            mapping['topright'] = letters[0]
            mapping['bottomright'] = letters[1]
    
    for letters in input:
        for letter in letters:
            if letter in mapping.values():
                continue
                

    return mapping

def findNumSum(input, output):
    numSum = 0

    letterPositions = mappingNum(input)

    print(letterPositions)

    return numSum

totalSum = 0

for index in range(len(content)):
    totalSum += findNumSum(content[index][0], content[index][1])

print(totalSum)