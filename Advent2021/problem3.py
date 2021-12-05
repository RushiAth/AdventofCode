def binaryToDecimal(binary):
     
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1

    return decimal   

def calculate1and0(content):
    lst = []
    gamma = ''
    epsilon = ''

    for num in range(12):
        countOne = 0
        countZero = 0

        for index in range(len(content)): 
        
            if int(content[index][num]) == 1:
                countOne += 1
            else:
                countZero += 1
            
        if countZero > countOne:
            gamma = gamma + '0'
            epsilon = epsilon + '1'
        else: 
            gamma = gamma + '1'
            epsilon = epsilon + '0'

        lst.append((countZero, countOne))

    return gamma, epsilon, lst

handIn = open('input3.txt')
content = handIn.readlines()
handIn.close()

#problem 1
gamma, epsilon, lst = calculate1and0(content)
print(binaryToDecimal(int(gamma)) * binaryToDecimal(int(epsilon)))


#problem 2
oxygenLst, COLst = content.copy(), content.copy()

for num in range(12):
    removing = []
    lst = calculate1and0(oxygenLst)[2]

    if lst[num][0] <= lst[num][1]:
        lookingfor = '1'
    else: 
        lookingfor = '0'

    for index in range(len(oxygenLst)):
        if oxygenLst[index][num] != lookingfor:
            removing.append(oxygenLst[index])

    for num2 in removing:
        oxygenLst.remove(num2)

    if len(oxygenLst) == 1:
        break

oxygenRating = binaryToDecimal(int(oxygenLst[0].strip()))


for num in range(12):
    removing = []
    lst = calculate1and0(COLst)[2]

    if lst[num][0] <= lst[num][1]:
        lookingfor = '0'
    else: 
        lookingfor = '1'

    for index in range(len(COLst)):
        if COLst[index][num] != lookingfor:
            removing.append(COLst[index])

    for num2 in removing:
        COLst.remove(num2)

    if len(COLst) == 1:
        break
        
CORating = binaryToDecimal(int(COLst[0].strip()))

print(oxygenRating*CORating)