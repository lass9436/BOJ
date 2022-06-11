import sys
T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    arr = []
    arr.append([0] + list(map(int, sys.stdin.readline().split())))
    arr.append([0] + list(map(int, sys.stdin.readline().split())))
    dp = [[0 for _ in range(N+1)] for _ in range(2)]
    
    dp[0][1] = arr[0][1]
    dp[1][1] = arr[1][1]
    
    for i in range(2, N+1):
        dp[0][i] = arr[0][i] + max(dp[1][i-1], dp[1][i-2], dp[0][i-2])
        dp[1][i] = arr[1][i] + max(dp[0][i-1], dp[0][i-2], dp[1][i-2])
    
    print(max(dp[0][N], dp[1][N]))