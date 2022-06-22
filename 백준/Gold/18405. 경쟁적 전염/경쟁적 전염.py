import sys
from heapq import heappop, heappush
N, K = map(int, sys.stdin.readline().split())
area = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
S, X, Y = map(int, sys.stdin.readline().split())

visited = [[False for _ in range(N)] for _ in range(N)]
move = [[1, 0], [-1, 0], [0, 1], [0, -1]]
heap = []

for i in range(N):
    for j in range(N):
        if area[i][j] > 0:
            heappush(heap, (0, area[i][j], i, j))
while heap:
    t, k, r, c = heappop(heap)
    if t == S:
        break
    for d in range(4):
        dr = r + move[d][0]
        dc = c + move[d][1]
        if 0 <= dr < N and 0 <= dc < N and area[dr][dc] == 0:
            area[dr][dc] = k
            heappush(heap, (t + 1, k, dr, dc))
            
print(area[X-1][Y-1])