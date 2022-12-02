f = open("day8.txt", "r")
lines = f.readlines()

cnts = [0 for i in range(10)]
for line in lines:
    arr = line.split()
    tmp = []
    for i in range(len(arr)):
        # if(arr[i]!='|'):
        #     print(i)
        if i>10:
            lens = len(arr[i])
            # sort all characters in string python
            # https://www.geeksforgeeks.org/sort-all-characters-in-string-python/
            arr[i] = ''.join(sorted(arr[i]))
            if(lens == 2):
                cnts[2]+=1
                tmp.append(arr[i]+'1')
            elif(lens==3):
                cnts[7]+=1
                tmp.append(arr[i]+'7')
            elif(lens==4):
                cnts[4]+=1
                tmp.append(arr[i]+'4')
            elif(lens==7):
                tmp.append(arr[i]+'8')
                cnts[8]+=1
            else:
                tmp.append(arr[i])
    print(tmp)

import numpy as np
print(np.sum(cnts))
