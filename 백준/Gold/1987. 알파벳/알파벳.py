import sys
R, C = map(int, sys.stdin.readline().split())
area = [list(sys.stdin.readline().rstrip()) for _ in range(R)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
answer = 0
alpha = set()

def dfs(r, c, depth):
    global answer
    answer = max(answer, depth)
    for i in range(4):
        dr = r + dx[i]
        dc = c + dy[i]
        if 0 <= dr < R and 0 <= dc < C and area[dr][dc] not in alpha:
            alpha.add(area[dr][dc])
            dfs(dr, dc, depth+1)
            alpha.remove(area[dr][dc])

alpha.add(area[0][0])
dfs(0,0,1)
print(answer)