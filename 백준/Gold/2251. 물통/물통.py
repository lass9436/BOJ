import sys
from collections import deque
A, B, C = map(int, sys.stdin.readline().split())
visited = [[False for _ in range(C+1)] for _ in range(C+1)]
q = deque()
q.append((0, 0))
answer = []

while q:
    x, y = q.popleft()
    if visited[x][y]:
        continue
    visited[x][y] = True
    if x == 0 and C - x - y not in answer:
        answer.append(C - x - y)
    #a->b
    water = min(B - y, x)
    q.append((x - water, y + water))
    #a->c
    water = min(x + y, x)
    q.append((x - water, y))
    #b->a
    water = min(A - x, y)
    q.append((x + water, y - water))
    #b->c
    water = min(x + y, y)
    q.append((x, y - water))
    #c->a
    water = min(C - x - y, A - x)
    q.append((x + water, y))
    #c->b
    water = min(C - x - y, B - y)
    q.append((x, y + water))
    
answer.sort()
print(*answer)