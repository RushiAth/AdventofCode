handIn = open('testingInput.txt')
content = [line.strip() for line in handIn.readlines()]

caves = {}

for line in content:
    one, two = line.split('-')
    caves[one] = caves.get(one, list())
    caves[two] = caves.get(two, list())
    caves[one].append(two)
    caves[two].append(one)

def findPath(position, dict):
    None


currentPos = 'start'
alreadyVisited = ['start']

for loc in caves['start']:
    findPath(currentPos, caves)


print(caves)