handIn = open('input8.txt')

content = [(line.strip()).split(' | ') for line in (handIn.readlines())]
counter = 0

for index in range(len(content)):
    value = content[index][1].split()

    for i in value:
        if len(i) in [2, 3, 4, 7]:
            counter += 1

print(counter)