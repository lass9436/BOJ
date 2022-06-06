import sys
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
X = int(sys.stdin.readline())
arr[X] = -2
answer = 0

def dfs(n):
    global answer, arr
    isLeaf = True
    for i in range(N):
        if arr[i] == n:
            dfs(i)
            isLeaf = False
    if n >= 0 and isLeaf:
        answer += 1

dfs(-1)

print(answer)