import sys
num, E, W, S, N = map(int, sys.stdin.readline().split())
visited = [[0 for _ in range(30)] for _ in range(30)]
x = 0
y = 0
answer = 0
def dfs(count, depth):
    global visited, x, y, answer
    if depth == num:
        answer += count
        return
    if E > 0:
        x = x + 1
        if not visited[x][y]:
            visited[x][y] = True
            dfs(count*(E/100), depth+1)
            visited[x][y] = False
        x = x - 1
    if W > 0:
        x = x - 1
        if not visited[x][y]:
            visited[x][y] = True
            dfs(count*(W/100), depth+1)
            visited[x][y] = False
        x = x + 1
    if S > 0:
        y = y - 1
        if not visited[x][y]:
            visited[x][y] = True
            dfs(count*(S/100), depth+1)
            visited[x][y] = False
        y = y + 1
    if N > 0:
        y = y + 1
        if not visited[x][y]:
            visited[x][y] = True
            dfs(count*(N/100), depth+1)
            visited[x][y] = False
        y = y - 1
visited[0][0] = True
dfs(1, 0)
print(answer)