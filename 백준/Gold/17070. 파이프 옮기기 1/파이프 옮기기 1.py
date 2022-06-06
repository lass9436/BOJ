import sys
sys.setrecursionlimit(10**5)
N = int(sys.stdin.readline())
area = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

answer = 0

def dfs(r, c, di):
    global N, answer
    if r == c == N - 1:
        answer += 1
    if di == 0:
        if possible(r, c+1, 0):
            dfs(r, c+1, 0)
        if possible(r+1, c+1, 1):
            dfs(r+1, c+1, 1)
    if di == 1:
        if possible(r, c+1, 0):
            dfs(r, c+1, 0)
        if possible(r+1, c+1, 1):
            dfs(r+1, c+1, 1)
        if possible(r+1, c, 2):
            dfs(r+1, c, 2)            
    if di == 2:
        if possible(r+1, c+1, 1):
            dfs(r+1, c+1, 1)
        if possible(r+1, c, 2):
            dfs(r+1, c, 2)       
            
def possible(r, c, di):
    global area
    if not (0 <= r < N and 0 <= c < N):
        return False
    if di == 0 or di == 2:
        if area[r][c] == 1:
            return False
    if di == 1:
        if area[r][c] == 1 or area[r-1][c] == 1 or area[r][c-1] == 1:
            return False
    return True        
    
dfs(0, 1, 0)
print(answer)