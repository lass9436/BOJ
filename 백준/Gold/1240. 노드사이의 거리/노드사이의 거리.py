import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())
adj = [[] for _ in range(N+1)]
for _ in range(N-1):
    u, v, w = map(int, sys.stdin.readline().split())
    adj[u].append((v, w))
    adj[v].append((u, w))
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    visited = [False] * (N + 1)
    q = deque()
    q.append((u, 0))
    while q:
        curNode, curWeight = q.popleft()
        if curNode == v:
            print(curWeight)
            break
        if visited[curNode]:
            continue
        visited[curNode] = True
        for nextNode, nextWeight in adj[curNode]:
            q.append((nextNode, curWeight + nextWeight))