f = open("day5.txt", "r")
lines = f.readlines()

grid = [ [0 for i in range(1000)] for j in range(1000)]
# print(grid)

for line in lines:
    line = line.strip()
    arr = line.split(" ")
    print(arr)
    arr2 = arr[0].split(',')
    arr3 = arr[2].split(',')
    x1, y1 = int(arr2[0]), int(arr2[1])
    x2, y2 = int(arr3[0]), int(arr3[1])
    print(x1,y1,x2,y2)

    t1 = min(x1, x2)
    t2 = max(x1,x2)
    s1 = min(y1, y2)
    s2 = max(y1, y2)

    if t2 >= 1000 or s2 >= 1000:
        exit()


    if t1==t2 or s1==s2:
        for i in range(t1,t2+1):
            for j in range(s1, s2+1):
                grid[i][j]+=1
    else:
        if x1>x2:
            tmp = x1
            x1 = x2
            x2 = tmp
            tmp = y1
            y1 = y2
            y2 = tmp
        if abs(t2-t1) == abs(s2-s1):
            print(x1,y1,x2,y2)
            if y1<y2:
                for k in range(y2-y1+1):
                    grid[x1+k][y1+k]+=1
            else:
                for k in range(y1-y2+1):
                    grid[x1+k][y1-k]+=1

# print(grid)
cnt = 0
for i in range(1000):
    for j in range(1000):
        if grid[i][j] > 1:
            cnt +=1
print(cnt)

