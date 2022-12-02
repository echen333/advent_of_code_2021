f = open("day12.txt", "r")
lines = f.readlines()

adj = {}
cnt = 0

def dfs(a, b, smalls):
    # print(a,b, adj[a])
    if a == 'end':
        global cnt
        cnt += 1
        # print(b, cnt)
        return
    for x in adj[a]:
        c = b.copy()
        c.append(x)
        if x.isupper():
            dfs(x, c, smalls)
        elif b.count(x) == 1  and x != "start" and smalls == False:
            dfs(x,c, True)
        elif b.count(x) == 0:
            dfs(x,c, smalls)


# map<str, list[]
for line in lines:
    line = line.strip()
    tmp = line.split('-')
    if tmp[0] not in adj:
        adj[tmp[0]] = []
    if tmp[1] not in adj:
        adj[tmp[1]] = []
    adj[tmp[0]].append(tmp[1])
    adj[tmp[1]].append(tmp[0])

dfs("start", ["start"], False)
print(cnt)