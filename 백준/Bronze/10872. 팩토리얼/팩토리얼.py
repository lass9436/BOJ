N = int(input())

dp = [0 for _ in range(N+1)]

dp[0] = 1

if N >= 1:
    dp[1] = 1

if N >= 2:
    for i in range(2, N+1):
        dp[i] = i * dp[i-1]
    
print(dp[N])