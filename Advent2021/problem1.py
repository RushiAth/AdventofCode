handIn = open('input1.txt')

content = handIn.read()
content = content.split()

#making all ints
for num in range(0, len(content)):
    content[num] = int(content[num])

#puzzle 1
counter = 0

for num in range(1, len(content)-1):
    if content[num] > content[num-1]:
        counter += 1

print(counter)


#puzzle 2
counter = 0

for num in range(0, len(content)-3):
    if (content[num+1] + content[num+2] + content[num+3]) > (content[num] + content[num+1] + content[num+2]):
        counter += 1

print(counter)

handIn.close()