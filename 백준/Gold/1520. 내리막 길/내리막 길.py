import sys
sys.setrecursionlimit(10**7)

R, C = map(int, sys.stdin.readline().split())

world = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]
dp = [[-1] * C for _ in range(R)]
move = [[0,1], [0, -1], [1,0], [-1, 0]]

def dp_bruteForce(r, c):
    if dp[r][c] != -1:
        return dp[r][c]
    if r == R - 1 and c == C - 1:
        return 1
    dp[r][c] = 0
    for i in range(0, 4):
        dr = r + move[i][0]
        dc = c + move[i][1]
        if 0 <= dr < R and 0 <= dc < C and world[dr][dc] < world[r][c]:
            dp[r][c] += dp_bruteForce(dr, dc)
    return dp[r][c]

print(dp_bruteForce(0, 0))