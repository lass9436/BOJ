import sys
N = int(sys.stdin.readline())
dp = [[0 for _ in range(N)] for _ in range(N+1)]
for i in range(1, N+1):
    arr = list(map(int, sys.stdin.readline().split()))
    for j in range(len(arr)):
        if j == 0:
            dp[i][j] = arr[j] + dp[i-1][j]
        else:
            dp[i][j] = arr[j] + max(dp[i-1][j], dp[i-1][j-1])
            
print(max(dp[N]))