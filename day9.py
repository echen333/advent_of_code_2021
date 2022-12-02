f = open("day9.txt", "r")
lines = f.readlines()
arr = []

for line in lines:
    chars = line.strip()
    tmp = []
    # turn to char list
    for char in chars:
        tmp.append(char)
    tmp = [int(x) for x in tmp]
    arr.append(tmp)

print(arr)

n= len(arr)
m = len(arr[0])

def check(x, y):
    return x>=0 and x<n and y>=0 and y<m

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

sum=0
lows = []
for i in range(n):
    for j in range(m):
        ok = True
        for k in range(4):
            ni = i+dx[k]
            nj = j+dy[k]
            if check(ni, nj) and arr[ni][nj] <= arr[i][j]:
                ok = False
        if ok:
            sum += arr[i][j] + 1
            lows.append((i, j))

gr = [ [-1 for i in range(m)] for j in range(n)]
def dfs(x, y, grc):
    gr[x][y]=grc
    for k in range(4):
        ni = x+dx[k]
        nj = y+dy[k]
        if check(ni, nj) and gr[ni][nj]==-1 and arr[ni][nj] >= arr[x][y] and arr[ni][nj]!=9:
            dfs(ni, nj, grc)

cnt = 1
for low in lows:
    x, y = low
    if gr[x][y] == -1:
        dfs(x, y, cnt)
        cnt += 1

print(cnt)

sizing = [0 for i in range(cnt+1)]
for i in range(n):
    for j in range(m):
        if gr[i][j] != -1:
            sizing[gr[i][j]] += 1

# sort sizings
sizing.sort()
print(sizing)

#print grid
# for i in range(n):
#     for j in range(m):
#         print(gr[i][j], end=" ")
#     print()