import sys
from collections import deque
sys.setrecursionlimit(10**7)

N, M = map(int, sys.stdin.readline().split())
adj = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    adj[u].append(v)
    adj[v].append(u)

visited = [False] * N
chk = False

def dfs(cur, depth):
    global visited, adj, chk
    if depth == 4:
        print(1)
        exit()
    for i in adj[cur]:
        if not visited[i]:
            visited[i] = True
            dfs(i, depth + 1)
            visited[i] = False

def solve():
    global N, chk
    for i in range(N):
        visited[i] = True
        dfs(i, 0)
        visited[i] = False
    print(0)
    
solve()