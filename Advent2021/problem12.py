handIn = open('input12.txt')
content = [line.strip() for line in handIn.readlines()]

caves = {}
pathCount = 0

for line in content:
    one, two = line.split('-')
    caves[one] = caves.get(one, list())
    caves[two] = caves.get(two, list())
    caves[one].append(two)
    caves[two].append(one)


def findPath(position, alreadyVisited) -> bool:

    global pathCount

    if position == 'end':
        pathCount += 1
        return True

    for loc in caves[position]:

        if loc not in alreadyVisited:
            if position.islower() and position not in alreadyVisited:
                alreadyVisited = alreadyVisited + (position,)

            findPath(loc, alreadyVisited)

    return False
    

findPath('start', ('start',))

print(pathCount)