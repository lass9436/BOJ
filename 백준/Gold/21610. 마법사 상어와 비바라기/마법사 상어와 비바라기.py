import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())
area = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
order = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
move = [[0,0],[0,-1],[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1]]
diagonal = [[-1,-1], [1,1], [1,-1], [-1,1]]
visited = [[False for _ in range(N)] for _ in range(N)]
q = deque()
q.append((N-1,0))
q.append((N-1,1))
q.append((N-2,0))
q.append((N-2,1))

for (d, s) in order:
    visited = [[False for _ in range(N)] for _ in range(N)]
    n = len(q)
    for _ in range(n):
        r, c = q.popleft()
        dr = r + move[d][0]*(s%N)
        dc = c + move[d][1]*(s%N)
        dr = (dr + N)%N
        dc = (dc + N)%N
        area[dr][dc] += 1
        q.append((dr,dc))
    for _ in range(n):
        r, c = q.popleft()
        visited[r][c] = True
        r = (N + r) % N
        c = (N + c) % N
        count = 0
        for (dr, dc) in diagonal:
            xr = r + dr
            xc = c + dc
            if 0 <= xr < N and 0 <= xc < N:
                if area[xr][xc] > 0:
                    count += 1
        area[r][c] += count
    for i in range(N):
        for j in range(N):
            if area[i][j] >= 2 and not visited[i][j]:
                area[i][j] -= 2
                q.append((i,j))
answer = 0
for i in range(N):
    for j in range(N):
        answer += area[i][j]
print(answer)