f = open("day14.txt", "r")
lines = f.readlines()

st = ""
rule = {}
for ind, line in enumerate(lines):
    line = line.strip()
    if ind ==0:
        st = line.strip()
    elif ind>1:
        tmp = line.split(" ")
        print(tmp)
        rule[(tmp[0][0], tmp[0][1])] = tmp[2]


print(rule)
cur = {}
cnts = [0 for i in range(26)]
for i in range(len(st)):
    cnts[ord(st[i])-ord('A')] += 1
    if i+1<len(st):
        if (st[i], st[i+1]) in cur:
            cur[(st[i], st[i+1])] += 1
        else:
            cur[(st[i], st[i+1])] = 1

print(cur)
for i in range(40):
    print(cur)
    new_cur = {}
    for key, val in cur.items():
        if key in rule:
            cnts[ord(rule[key])-ord('A')] += val

            new_cur[(key[0], rule[key])] = new_cur.get((key[0], rule[key]), 0) + val
            new_cur[(rule[key], key[1])] = new_cur.get((rule[key], key[1]), 0) + val
        else:
            new_cur[key] = val
            # if i+1<len(st):
            #     if (key[1], rule[key]) in cur:
            #         cur[(key[1], rule[key])] += val
            #     else:
            #         cur[(key[1], rule[key])] = val
    cur = new_cur
    # for j in range(len(st)):
    #     tmp += st[j]
    #     if j+1 < len(st):
    #         tmp += rule[(st[j], st[j+1])]
    # st = tmp
    # print(st)

# for i in range(len(st)):
#     cnts[ord(st[i])-ord('A')] += 1
# for i in range(26):
#     cnt = st.count(chr(ord('A')+i))
#     cnts.append(cnt)

print(cnts)

import numpy as np
print(np.min(cnts))
print(np.max(cnts))
print(np.max(cnts)-np.min(cnts))

mn = 1e18
for x in cnts:
    print(x)
    if x<mn and x>0:
        mn = x
        print("MN",mn)

print(np.max(cnts)-mn)