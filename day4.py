f = open("day4.txt", "r")
lines = f.readlines()

nums = []
cur_board = []
boards = []
for ind, line in enumerate(lines):
    tmp = line.strip()
    if tmp == "":
        continue
    if ind == 0:
        nums = tmp.split(',')
        nums = [int(x) for x in nums]
    else:
        tmp2 = tmp.split()
        tmp2 = [int(x) for x in tmp2]
        if len(cur_board) >= 5:
            boards.append(cur_board)
            cur_board = []
        cur_board.append(tmp2)

if len(cur_board) >= 5:
    boards.append(cur_board)

def check(board):
    for i in range(5):
        ok = True
        for j in range(5):
            if not board[i][j]:
                ok = False
        if ok:
            return ok
    for i in range(5):
        ok = True
        for j in range(5):
            if not board[j][i]:
                ok = False
        if ok:
            return ok
    return False

def calc(board, ok):
    sum = 0
    for i in range(5):
        for j in range(5):
            if not ok[i][j]:
                sum += board[i][j]
    return sum

cnts = []
scores = []
for board in boards:
    aight = [ [False for i in range(5)] for j in range(5)]
    print(board, aight)
    done = False
    for ind, i in enumerate(nums):
        for k in range(5):
            for l in range(5):
                if board[k][l] == i:
                    aight[k][l] = True
                    if check(aight) and not done:
                        print(aight)
                        cnts.append(ind)
                        scores.append(calc(board, aight)*i)
                        done = True
        
            

import numpy as np
min_ind = np.argmin(cnts)
max_ind = np.argmax(cnts)
print(cnts[min_ind], scores[min_ind])
print(min_ind, scores[min_ind])
print(max_ind, scores[max_ind])