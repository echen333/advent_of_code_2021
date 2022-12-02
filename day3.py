f = open("day3.txt", "r")
lines = f.readlines()
arr = []
for line in lines:
    tmp = line.strip()
    arr.append(tmp)

t1, t2 = 0, 0
tot1 = arr
tot2 = arr
for i in range(len(arr[0])):
    print(tot1, tot2)
    cnt = 0
    for j in range(len(tot1)):
        if tot1[j][i] == '1':
            cnt += 1
    cnt2 = len(tot1) - cnt
    tmp1 = []
    if cnt >= cnt2:
        for j in range(len(tot1)):
            if tot1[j][i] == '1':
                tmp1.append(tot1[j])
        tot1 = tmp1
    else:
        for j in range(len(tot1)):
            if tot1[j][i] == '0':
                tmp1.append(tot1[j])
        tot1 = tmp1
    
    cnt = 0
    for j in range(len(tot2)):
        if tot2[j][i] == '1':
            cnt += 1
    cnt2 = len(tot2) - cnt
    tmp2 = []
    if cnt < cnt2:
        for j in range(len(tot2)):
            if tot2[j][i] == '1':
                tmp2.append(tot2[j])
        tot2 = tmp2
    else:
        for j in range(len(tot2)):
            if tot2[j][i] == '0':
                tmp2.append(tot2[j])
        tot2 = tmp2


print(tot1)
print(tot2)