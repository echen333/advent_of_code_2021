x, y = 0, 0

f = open("day2.txt", "r")
lines = f.readlines()
aim  = 0
for line in lines:
    tmp = line.split()
    if(tmp[0] == "forward"):
        x += int(tmp[1])
        y += aim*int(tmp[1])
    if(tmp[0] == "down"):
        aim += int(tmp[1])
    if(tmp[0] == "up"):
        aim -= int(tmp[1])
    print(x,y)

print(x*y)