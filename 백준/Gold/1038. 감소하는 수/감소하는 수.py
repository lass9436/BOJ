import sys
N = int(sys.stdin.readline())
lastNum = 0
find = False

def dfs(num, depth):
    global lastNum, find
    if lastNum == 1000001:
        return
    if find:
        return
    if depth == len(num):
        if lastNum == N:
            find = True
            print(num)
        lastNum += 1
        return
    
    last = 10
    if len(num) > 0:
        last = int(num[-1])
    for i in range(0, last):
        dfs(num + str(i), depth)
    
for i in range(1, 20):
    dfs("", i)
if not find:
    print(-1)