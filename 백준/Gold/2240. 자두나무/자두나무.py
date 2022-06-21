import sys
N, M = map(int, sys.stdin.readline().split())
arr = [0] + [int(sys.stdin.readline()) for _ in range(N)]
dp = [[0 for _ in range(M+1)] for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(M+1):
        if j > 0:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1])
        else:
            dp[i][j] = dp[i-1][j]
        pos = j % 2
        if arr[i] == 1 and pos == 0:
            dp[i][j] += 1
        elif arr[i] == 2 and pos == 1:
            dp[i][j] += 1
            
print(max(dp[N]))