f = open("day13.txt", "r")
lines = f.readlines()
import numpy as np

data = []
done = False
folds = []
for line in lines:
    line = line.strip()
    if not done:
        tmp = line.split(',')
        if(tmp[0]==''):
            done = True
            continue
        data.append([int(tmp[0]), int(tmp[1])])
    else:
        tmp = line.split()
        tmp2 = tmp[2].split('=')
        cur = False
        if tmp2[0]=='x':
            cur = False
        else:
            cur = True
        folds.append((cur, int(tmp2[1])))


for fold in folds:
    new_data = set()
    for pt in data:
        if fold[0] == False:
            if pt[0] < fold[1]:
                new_data.add((pt[0], pt[1]))
            else:
                new_data.add((fold[1]-abs(pt[0]-fold[1]), pt[1]))
        else:
            if pt[1] < fold[1]:
                new_data.add((pt[0], pt[1]))
            else:
                new_data.add((pt[0], fold[1]-abs(pt[1]-fold[1])))
    data = new_data

grid = np.zeros((100, 100))
for pt in data:
    grid[pt[0], pt[1]] = 1

for row in grid:
    for col in row:
        if col == 1:
            print('#', end='')
        else:
            print('.', end='')
    print()