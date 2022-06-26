import sys
from collections import deque
N, M, T = map(int, sys.stdin.readline().split())
area = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]
move = [[1,0],[-1,0],[0,1],[0,-1]]
answer = sys.maxsize
q = deque()
q.append((0,0,0))
while q:
    r, c, t = q.popleft()   
    if t > T:
        continue
    if r == N-1 and c == M-1:
        answer = min(answer, t)
        continue
    if area[r][c] == 2:
        answer = min(answer, t + (N - 1 - r) + (M - 1 - c))
    for i in range(4):
        dr = r + move[i][0]
        dc = c + move[i][1]
        if 0 <= dr < N and 0 <= dc < M and not visited[dr][dc] and area[dr][dc] != 1:
            visited[dr][dc] = True
            q.append((dr,dc,t+1))
            
print(answer if answer <= T else "Fail")