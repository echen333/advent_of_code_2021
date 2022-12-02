f = open("day7.txt", "r")
lines = f.readlines()
arr = lines[0].split(',')
arr = [int(x) for x in arr]

print(arr)
import numpy as np

print(len(arr), np.min(arr), np.max(arr))

# sum = 0
# for i in range(len(arr)):
#     sum += abs(arr[i]-tmp)

mn = 1e9
ans = 0
for tmp in range(0, 2000):
    sum = 0
    for i in range(len(arr)):
        tmp3 = abs(arr[i]-tmp)
        sum += tmp3*(tmp3+1)/2
    # print(tmp, sum)
    if sum<mn:
        mn = sum
        ans = tmp
    # print(tmp, sum, mn)

print(mn, tmp, ans)