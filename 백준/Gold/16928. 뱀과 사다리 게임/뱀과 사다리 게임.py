import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())
move = [0] * 101
visited = [False] * 101
for i in range(101):
    move[i] = i
for _ in range(N + M):
    u, v = map(int, sys.stdin.readline().split())
    move[u] = v
q = deque()
q.append((1, 0))
while q:
    cur, depth = q.popleft()
    if cur == 100:
        print(depth)
        exit()
    if cur > 100:
        continue
    if visited[cur]:
        continue
    visited[cur] = True
    cur = move[cur]
    q.append((cur + 1, depth + 1))
    q.append((cur + 2, depth + 1))
    q.append((cur + 3, depth + 1))
    q.append((cur + 4, depth + 1))
    q.append((cur + 5, depth + 1))
    q.append((cur + 6, depth + 1))