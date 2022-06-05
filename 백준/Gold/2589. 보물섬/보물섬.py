import sys
from collections import deque
R, C = map(int, sys.stdin.readline().split())
area = [list(sys.stdin.readline().rstrip()) for _ in range(R)]
move = [[1, 0], [-1, 0], [0, 1], [0, -1]]
answer = 0

for i in range(R):
    for j in range(C):
        if area[i][j] == "L":
            visited = [[False for _ in range(C)] for _ in range(R)]
            q = deque()
            q.append((i, j, 0))
            while q:
                r, c, count = q.popleft()
                if visited[r][c]:
                    continue
                visited[r][c] = True
                answer = max(answer, count)
                for k in range(4):
                    dr = r + move[k][0]
                    dc = c + move[k][1]
                    if 0 <= dr < R and 0 <= dc < C and area[dr][dc] == "L":
                        q.append((dr, dc, count + 1))
            
print(answer)