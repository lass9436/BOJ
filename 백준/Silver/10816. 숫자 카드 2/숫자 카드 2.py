import sys
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split(" ")))
dic = {}
for i in arr:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
M = int(sys.stdin.readline())
arr2 = list(map(int, sys.stdin.readline().split(" ")))
answer = []
for i in arr2:
    if i in dic:
        answer.append(dic[i])
    else:
        answer.append(0)
print(*answer)