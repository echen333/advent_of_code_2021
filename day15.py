f = open("day15.txt", "r")
lines = f.readlines()

arr=[]
for line in lines:
    tmp = line.strip()
    tmps =[]
    for l in range(5):
        for j in range(len(tmp)):
            tmps.append(int(tmp[j]))
    arr.append(tmps)

print(arr)

arrs = []
for k in range(5):
    for t in arr:
        arrs.append(t)

arr = arrs

print(arrs)

best = [[1e9 for i in range(len(arr[0]))] for j in range(len(arr))]

pq = []
pq.append((0, (0,0)))
best[0][0] = 0

def check(x, y):
    return x>=0 and x<len(arr) and y>=0 and y<len(arr[0])

# for i in range(len(arr)):
#     for j in range(len(arr[0])):
#         if i > 0:
#             best[i][j] = min(best[i][j], best[i-1][j] + arr[i][j])
#         if j > 0:
#             best[i][j] = min(best[i][j], best[i][j-1] + arr[i][j])
    
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
while len(pq) > 0:
    tmp = pq.pop(0)
    x = tmp[1][0]
    y = tmp[1][1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if check(nx, ny) and best[nx][ny] > best[x][y] + arr[nx][ny]:
            best[nx][ny] = best[x][y] + arr[nx][ny]
            pq.append((best[nx][ny], (nx, ny)))

# print(best)
print(best[len(arr)-1][len(arr[0])-1])