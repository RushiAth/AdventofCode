handIn = open('input01.txt')

content = (handIn.read()).split()

for num in range(len(content)):
    content[num] = int(content[num])

#part 1
counter = 0

for num in range(1, len(content)-1):
    if content[num] > content[num-1]:
        counter += 1

print(counter)

#part 2
counter = 0

for num in range(0, len(content)-3):
    if (content[num+1] + content[num+2] + content[num+3]) > (content[num] + content[num+1] + content[num+2]):
        counter += 1

print(counter)