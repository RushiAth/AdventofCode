handIn = open('testInput.txt')

lines = (handIn.read()).split('\n')
i = 0

#Taking in crate positions
while(lines[i] != ""):
    i += 1

crates = lines[:i]
numCols = len(crates[-1].split())
