import sys
from collections import deque

R, C = map(int, sys.stdin.readline().split())

maze = [list(map(int, sys.stdin.readline().strip('\n'))) for _ in range(R)]

queue = deque([])

queue.append([0, 0, 1])

visited = [[False] * C for _ in range(R)]

while queue:
    current = queue.popleft()
    r = current[0]
    c = current[1]
    count = current[2]
    if visited[r][c] or maze[r][c] == 0:
        continue
    if r == R - 1 and c == C - 1:
        print(count)
        break
    visited[r][c] = True
    
    if 0 <= r + 1 < R and 0 <= c < C:
        queue.append([r + 1, c, count+1])
    if 0 <= r - 1 < R and 0 <= c < C:
        queue.append([r - 1, c, count+1])
    if 0 <= r < R and 0 <= c + 1 < C:
        queue.append([r, c + 1, count+1])
    if 0 <= r < R and 0 <= c - 1 < C:
        queue.append([r, c - 1, count+1])