import sys
from collections import deque

C, R = map(int, sys.stdin.readline().split())

world = [list(map(int, sys.stdin.readline().split())) for r in range(R)]
visited = [[False for c in range(C)] for r in range(R)]
move = [[0,1], [0,-1], [1,0], [-1,0]]
queue = deque()
maxDay = 0

for r in range(R):
    for c in range(C):
        if world[r][c] == 1:
            visited[r][c] = True
            queue.append([r, c, 0])

while queue:
    cur = queue.popleft()
    r = cur[0]
    c = cur[1]
    day = cur[2]
    maxDay = max(maxDay, day)
    for i in range(4):
        dr = r + move[i][0]
        dc = c + move[i][1]
        if 0 <= dr < R and 0 <= dc < C and not visited[dr][dc] and world[dr][dc] == 0:
            visited[dr][dc] = True
            world[dr][dc] = 1
            queue.append([dr, dc, day+1])

for i in range(R):
    for j in range(C):
        if world[i][j] == 0:
            maxDay = -1

print(maxDay)