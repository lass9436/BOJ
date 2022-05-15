import sys
from collections import deque

N, M, S = map(int, sys.stdin.readline().split())

adj = [[False for j in range(N+1)] for i in range(N+1)]
visited = [False for i in range(N+1)]
visited2 = [False for i in range(N+1)]


for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    adj[i][j] = True
    adj[j][i] = True
    
def dfs(num):
    global N, adj, visited
    print(num, end=" ")
    
    for i in range(1, N+1):
        if not visited[i] and adj[num][i]:
            visited[i] = True
            dfs(i)

visited[S] = True            
dfs(S)

print()

queue = deque()
queue.append(S)
visited2[S] = True

while queue:
    n = queue.popleft()
    print(n, end=" ")
    
    for i in range(1, N+1):
        if not visited2[i] and adj[n][i]:
            visited2[i] = True
            queue.append(i)