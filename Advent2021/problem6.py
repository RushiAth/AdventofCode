from collections import Counter

def day(fishD):
    newFishD = {}

    for time in range(8, -1, -1):
        if time != 0:
            newFishD[time-1] = fishD[time]
        else:
            newFishD[8] = fishD[0]
            newFishD[6] += fishD[0]

    return newFishD

handIn = open('input6.txt')
content = Counter([int(num) for num in (handIn.read()).split(',')])

for i in range(256):
    content = day(content)

print(sum(content.values()))