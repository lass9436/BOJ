import sys

N, K = map(int, sys.stdin.readline().split())

dp = [[1 for _ in range(201)] for _ in range(201)]

for i in range(0, 201):
    dp[i][1] = 1
    dp[i][2] = i + 1
    
for i in range(1, 201):
    for j in range(3, 201):
        dp[i][j] = (dp[i-1][j] + dp[i][j-1]) 
        
print(dp[N][K]% 1000000000)