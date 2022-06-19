import sys
from collections import deque
N = int(sys.stdin.readline())
adj = [[] for _ in range(N+1)]
score = [0] * (N+1)
score[0] = sys.maxsize

def bfs(node, depth):
    global adj, score
    visited = [False] * (N+1)
    visited[node] = True
    q = deque()
    q.append((node, depth))
    while q:
        curNode, curDepth = q.popleft()
        score[node] = max(score[node], curDepth)
        for i in adj[curNode]:
            if not visited[i]:
                visited[i] = True
                q.append((i, curDepth + 1))

while True:
    u, v = map(int, sys.stdin.readline().split())
    if u == v == -1:
        break
    adj[u].append(v)
    adj[v].append(u)
for i in range(1, N+1):
    bfs(i, 0)

minScore = min(score)
count = 0
candiList = []

for i in range(1, N+1):
    if score[i] == minScore:
        count += 1
        candiList.append(i)
        
print(minScore, count)
print(*candiList)