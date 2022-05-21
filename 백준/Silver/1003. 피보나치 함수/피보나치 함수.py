import sys

N = int(sys.stdin.readline())

dp = [[0, 0] for _ in range(41)]

dp[0] = [1, 0]
dp[1] = [0, 1]

for i in range(2, 41):
    dp[i][0] = dp[i-2][0] + dp[i-1][0]
    dp[i][1] = dp[i-2][1] + dp[i-1][1]
    
for _ in range(N):
    num = int(sys.stdin.readline())
    print(dp[num][0], dp[num][1])