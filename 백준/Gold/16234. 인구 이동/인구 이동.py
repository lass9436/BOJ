import sys
from collections import deque
N, L, R = map(int, sys.stdin.readline().split())
area = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
move = [[0,1], [0,-1], [1,0], [-1, 0]]

answer = 0
while True:
    isContinue = False
    visited = [[False for _ in range(N)] for _ in range(N)]
    queue = deque()
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                queue.append((i, j))
                unionList = []
                sumPop = 0
                while queue:
                    r, c = queue.pop()
                    if visited[r][c]:
                        continue
                    visited[r][c] = True
                    unionList.append((r, c))
                    curPop = area[r][c]
                    sumPop += curPop
                    for t in range(4):
                        dr = r + move[t][0]
                        dc = c + move[t][1]
                        if 0 <= dr < N and 0 <= dc < N:
                            diff = abs(area[dr][dc] - curPop)
                            if L <= diff <= R:
                                isContinue = True
                                queue.append((dr, dc))
                meanPop = sumPop // len(unionList)
                for r, c in unionList:
                    area[r][c] = meanPop
    if not isContinue:
        break
    answer += 1
print(answer)