import sys
N = int(sys.stdin.readline())
dp = [[0, 0 ,0] for _ in range(N + 1)]
for i in range(1, N+1):
    r, g, b = map(int, sys.stdin.readline().split())
    dp[i][0] = r + min(dp[i-1][1], dp[i-1][2])
    dp[i][1] = g + min(dp[i-1][0], dp[i-1][2])
    dp[i][2] = b + min(dp[i-1][0], dp[i-1][1])
print(min(dp[N]))