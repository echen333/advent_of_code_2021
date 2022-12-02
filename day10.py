f = open("day10.txt", "r")
lines = f.readlines()

open = ['(','[','{', '<']
close = [')', ']', '}', '>']
sc = [3,57,1197,25137]
sc2 = [1,2,3,4]
score = 0
arr2=[]

import numpy as np

for line in lines:
    score2 = 0
    tmp = line.strip()
    stk = []
    bad = False
    for i in range(len(tmp)):
        print(stk)
        if tmp[i] in open:
            ind = open.index(tmp[i])
            stk.append(ind)
        else:
            ind = close.index(tmp[i])
            if len(stk) == 0:
                exit()
                break
            else:
                if stk[-1] == ind:
                    stk.pop()
                else:
                    bad = True
                    #  score += sc[ind]
                    # break
    
    if not bad:
        while len(stk) > 0:
            print(len(stk))
            ind = stk.pop()
            score2 = score2*5+sc2[ind]
        arr2.append(score2)


# print(score)
print(arr2)
print(np.median(arr2))