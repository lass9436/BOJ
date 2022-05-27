import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())
world = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
chicken = []
house = []
final = sys.maxsize

for i in range(N):
    for j in range(N):
        if world[i][j] == 1:
            house.append((i,j))
        elif world[i][j] == 2:
            chicken.append((i,j))

for chi in combinations(chicken, M):
    answer = 0
    for i, j in house:
        dist = sys.maxsize
        for k in range(M):
            r, c = chi[k]
            dist = min(dist, abs(i-r) + abs(j-c))
        answer += dist
    final = min(final, answer)
    
print(final)