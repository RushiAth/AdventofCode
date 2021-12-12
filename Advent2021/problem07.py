import math

def fuelCalc(crabs, position):
    sumFuel = 0
    
    for index in range(len(crabs)):
        positionFuel = 0

        for j in range(abs(crabs[index]-position)):
            positionFuel += (j+1)
            
        sumFuel += positionFuel
    return sumFuel

handIn = open('input07.txt')
content = [int(num) for num in (handIn.read()).split(',')]

fuelList = []

for i in range(max(content)+1):
    fuelList.append(fuelCalc(content, i))

print(min(fuelList))