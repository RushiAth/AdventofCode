def winCheck(board):    
    for i in range(5):
        countH = countV = 0

        for j in range(5):
            if board[i][j][1] == 1:
                countH += 1
            if board[j][i][1] == 1:
                countV += 1

        if countH == 5 or countV == 5:
            sum = 0

            for row in range(5):
                for column in range(5):
                    if board[row][column][1] == 0:
                        sum += board[row][column][0]
            
            return sum        

    return False

def playBingo(bingoOrder, boardLst):
    winningBoards = []
    numRightNow = 0
    
    for num in bingoOrder:
        num = int(num)

        for index in range(len(boardLst)):
            if boardLst[index] not in winningBoards:
                for row in boardLst[index]:
                    for j in row:
                        if j[0] == num:
                            j[1] = 1

            if winCheck(boardLst[index]) != False and boardLst[index] not in winningBoards:
                numRightNow = num
                winningBoards.append(boardLst[index])

                #return winCheck(boardLst[index]), num
    
    return winningBoards, numRightNow


handIn = open('input4.txt')

numOrder = (handIn.readline()).split(',')
content = handIn.readlines()

boards = []
counter = 0
boardNum = -1

#makes list of boards
for i in range(len(content)):
    line = content[i]

    if line == '\n': continue

    line = (line.strip()).split()

    for k in range(5):
        line[k] = [int(line[k]), 0]

    if counter%5 == 0:
        boards.append([])
        boardNum += 1

    boards[boardNum].append(line)
    counter += 1


#problem 1  == 31424
#sumOfUn, currentNum = playBingo(numOrder, boards)
#print(sumOfUn*currentNum)


#problem 2 = 23042
winningboards, currentNum = playBingo(numOrder, boards)
print(winCheck(winningboards[-1]) * currentNum)