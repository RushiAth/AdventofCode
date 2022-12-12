handIn = open('input02.txt')

rounds = (handIn.read()).split('\n')
plays = [[r[0], r[2]] for r in rounds[:-1]]

shapes = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3} 

#Part 1
win = ["A Y", "B Z", "C X"]
lose = ["A Z", "B X", "C Y"]

score = 0

for i in range(len(plays)):
    op = plays[i][0]
    me = plays[i][1]

    if shapes[op] == shapes[me]:
        score += shapes[me] + 3
    elif rounds[i] in win:
        score += shapes[me] + 6
    else: 
        score += shapes[me]

print(score)

#Part 2
winShapes = {"A": 2, "B": 3, "C": 1}
loseShapes = {"A": 3, "B": 1, "C": 2}

score = 0

for op, result in plays:

    if result == "Y":
        score += shapes[op] + 3
    elif result == "X":
        score += loseShapes[op]
    else:
        score += winShapes[op] + 6

print(score)