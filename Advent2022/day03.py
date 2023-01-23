handIn = open('input03.txt')

bags = (handIn.read()).split('\n')

#Part 1
halfBags = [[b[0:int(len(b)/2)], b[int(len(b)/2):]] for b in bags]

sumP = 0

for first, second in halfBags:
    common = [i for i in first if i in second][0]

    sumP += ord(common) - (38 if common.isupper() else 96)

print(sumP)


#Part 2
sumP = 0

for i in range(0, len(bags), 3):
    common = [j for j in bags[i] if (j in bags[i+1] and j in bags[i+2])][0]

    sumP += ord(common) - (38 if common.isupper() else 96)

print(sumP)