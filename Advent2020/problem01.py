handIn = open('Advent2020/input2020_1.txt')

content = handIn.read()
content = content.split()

#print(content)

for num in content:
    for num2 in content:
        if (int(num) + int(num2)) == 2020:
            print(int(num)*int(num2))

for num1 in content:
    for num2 in content:
        for num3 in content:
            if (int(num1) + int(num2) + int(num3)) == 2020:
                print(int(num1)*int(num2)*int(num3))

handIn.close()