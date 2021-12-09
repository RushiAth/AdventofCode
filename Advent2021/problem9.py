handIn = open('input9.txt')
content = [line.strip() for line in handIn.readlines()]

for index in range(len(content)):
    for index2 in range(len(content[index])):
        None