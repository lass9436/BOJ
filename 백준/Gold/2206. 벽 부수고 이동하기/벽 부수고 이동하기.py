import sys
from collections import deque

R, C = map(int, sys.stdin.readline().split())

maze = [list(map(int, list(sys.stdin.readline().strip("\n")))) for _ in range(R)]
visited = [[[False for canBreak in range(2)] for col in range(C)] for row in range(R)]


directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

queue = deque()

visited[0][0][1] = True
queue.append([0, 0, 1, 1])

answer = []

while queue:
    cur = queue.popleft()
    
    r = cur[0]
    c = cur[1]
    count = cur[2]
    canBreak = cur[3]
    
    if r == R -1 and c == C -1:
        answer.append(count)
        break
    
    for di in directions:
        dr = r + di[0]
        dc = c + di[1]
        if 0 <= dr < R and 0 <= dc < C:
            if maze[dr][dc] == 0 and not visited[dr][dc][canBreak]:
                visited[dr][dc][canBreak] = True
                queue.append([dr, dc, count+1, canBreak])
            if maze[dr][dc] == 1 and canBreak == 1 and not visited[dr][dc][canBreak - 1]:
                visited[dr][dc][canBreak - 1] = True
                queue.append([dr, dc, count+1, canBreak - 1])

try:
    print(min(answer))
except:
    print(-1)