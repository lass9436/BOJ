import sys
N, M = map(int, sys.stdin.readline().split())
arr = []
def dfs():
    global arr
    if len(arr) == M:
        print(*arr)
    for i in range(1, N+1):
        if len(arr) == 0:
            arr.append(i)
            dfs()
            arr.pop()
        else:
            pre = arr[-1]
            if i > pre:
                arr.append(i)
                dfs()
                arr.pop()       
dfs()