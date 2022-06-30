import sys
from collections import deque
R, C = map(int, sys.stdin.readline().split())
area = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(R)]
visited = [[False for _ in range(C)] for _ in range(R)]
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
water = 0

def bfs(r, c, height):
    global water
    visited = [[False for _ in range(C)] for _ in range(R)]
    q = deque()
    q.append((r, c))
    route = []
    visited[r][c] = True
    if height <= area[r][c]:
        return
    isPossible = True
    while q:
        curR, curC = q.popleft()
        route.append((curR, curC))
        for i in range(4):
            nextR = curR + dr[i]
            nextC = curC + dc[i]
            if 0 <= nextR < R and 0 <= nextC < C:
                if area[nextR][nextC] < height and not visited[nextR][nextC]:
                    visited[nextR][nextC] = True
                    q.append((nextR, nextC))
            else:
                isPossible = False
    if isPossible:
        for (x, y) in route:
            area[x][y] += 1
            water += 1

def solve(height):
    for r in range(R):
        for c in range(C):
            bfs(r, c, height)

for height in range(1, 10):
    solve(height)
    
print(water)