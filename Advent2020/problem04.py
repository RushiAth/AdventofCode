handIn = open('input2020_4.txt')

content = handIn.read()
content = content.split('\n\n')

valid = 0
fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

for index in range(len(content)):
    content[index] = content[index].split()
    counter = 0
    
    for ind in range(len(content[index])):
        if content[index][ind][:3] == 'byr' and 1920 <= int(content[index][ind][4:]) <= 2002:
            counter += 1
        elif content[index][ind][:3] == 'iyr' and 2010 <= int(content[index][ind][4:]) <= 2020:
            counter += 1
        elif content[index][ind][:3] == 'eyr' and 2020 <= int(content[index][ind][4:]) <= 2030:
            counter += 1
        elif content[index][ind][:3] == 'hgt':
            if content[index][ind][-2:] == 'in':
                if 59 <= int(content[index][ind][4:-2]) <= 76:
                    counter += 1
            elif content[index][ind][-2:] == 'cm':
                if 150 <= int(content[index][ind][4:-2]) <= 193:
                    counter += 1
        elif content[index][ind][:3] == 'hcl' and content[index][ind][4] == '#' and len(content[index][ind][5:]) == 6 and content[index][ind][5:].isalnum():
            counter += 1
        elif content[index][ind][:3] == 'ecl' and content[index][ind][4:] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            counter += 1
        elif content[index][ind][:3] == 'pid' and len(content[index][ind][4:]) == 9:
            counter += 1
            
    if counter == 7:
        valid += 1

print(valid)