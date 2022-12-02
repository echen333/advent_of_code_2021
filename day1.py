
cnt=0
lst = 1e9
f = open("day1.txt", "r")
lines = f.readlines()
arr = []
lst_count = 1e9
for line in lines:
    # tmp = input()
    arr.append(int(line))

for i in range(2, len(arr)):
    tmp = arr[i-1] + arr[i-2] + arr[i]
    if tmp > lst_count:
        cnt += 1
    lst_count = tmp
    print(cnt)