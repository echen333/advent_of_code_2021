f = open("day6.txt", "r")

lines = f.readlines()
arr = lines[0].split(',')
arr = [int(x) for x in arr]

cnts =[0 for i in range(10)]

for x in arr:
    cnts[x] +=1

print(cnts)

import numpy as np
for i in range(256):
    # print(i,cnts)
    cnt = cnts[0]
    for j in range(9):
        cnts[j]= cnts[j+1]
    cnts[8]+=cnt
    cnts[6]+=cnt

    print(i+1, cnts, cnt, np.sum(cnts))


print(np.sum(cnts))