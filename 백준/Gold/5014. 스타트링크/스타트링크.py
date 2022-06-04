import sys
from collections import deque
F, S, G, U, D = map(int, sys.stdin.readline().split())

visited = [False] * (F + 1)
q = deque()
q.append((S, 0))
find = False

while q:
    floor, count = q.popleft()
    if floor == G:
        print(count)
        find = True
        break
    if visited[floor]:
        continue
    visited[floor] = True
    if 0 < floor + U <= F:
        q.append((floor + U, count + 1))
    if 0 < floor - D <= F:        
        q.append((floor - D, count + 1))
        
if not find:
    print("use the stairs")