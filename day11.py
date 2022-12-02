f = open("day11.txt", "r")
lines = f.readlines()

arr = []
for line in lines:
    tmp = line.strip()
    ret = []
    for i in range(len(tmp)):
        ret.append(int(tmp[i]))
    arr.append(ret)

print(arr)

dx = [0, 0, 1, 1, 1, -1, -1, -1]
dy = [1, -1, 0, 1, -1, 0, 1, -1]
tmp = []

cnt=0

def go(x):
    for i in range(8):
        nx = x[0] + dx[i]
        ny = x[1] + dy[i]
        if check(nx, ny) and arr[nx][ny] != 0:
            arr[nx][ny]+=1
            if arr[nx][ny] > 9:
                arr[nx][ny] = 0
                global cnt
                cnt+=1
                go((nx,ny))

    return ret
    

def check(x, y):
    return x>=0 and x<len(arr) and y>=0 and y<len(arr[0])


fst = -1
for l in range(300):
    lst_cnt = cnt
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            arr[i][j] +=1
            if arr[i][j] == 10:
                arr[i][j]=0
                cnt+=1
                tmp.append((i,j))
    for i in range(len(tmp)):
        if arr[tmp[i][0]][tmp[i][1]] == 0:
            go(tmp[i])
    tmp = []
    print(cnt-lst_cnt)
    if cnt-lst_cnt == 100:
        print(l)
        # fst = l
        # break

print(cnt)
print(fst)