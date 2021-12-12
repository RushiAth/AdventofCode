handIn = open('input08.txt')
content = [(line.strip()).split(' | ') for line in (handIn.readlines())]

#part 1
counter = 0

for index in range(len(content)):
    for i in content[index][1].split():
        if len(i) in [2, 3, 4, 7]:
            counter += 1

print(counter)


#part 2
def mappingNum(input):
    mapping = {'top': '', 'middle': '', 'bottom': '', 'topright': '', 'topleft': '', 'bottomright': '', 'bottomleft': ''}

    input = [sorted(num) for num in input.split()]
    print(input)

    for letters in input:
        if len(letters) == 2:
            mapping['topright'] = letters[0]
            mapping['bottomright'] = letters[1]

        if len(letters) == 3:
            for letter in letters: 
                if letter not in mapping.values():
                    None
    
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