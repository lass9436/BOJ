import sys
sys.setrecursionlimit(10**7)

n = int(input())

dp = [[-1] * 3 for _ in range(n+1)]

def fn (n, k):
    if dp[n][k] > 0:
        return dp[n][k] % 9901
    if n == 1:
        return 1
    if k == 0:
        dp[n][k] = fn(n-1, 0) + fn(n-1, 1) + fn(n-1, 2)
        return dp[n][k]
    if k == 1:
        dp[n][k] = fn(n-1, 0) + fn(n-1, 2)
        return dp[n][k]
    if k == 2:
        dp[n][k] = fn(n-1, 0) + fn(n-1, 1)
        return dp[n][k]

answer = (fn(n, 0) + fn(n, 1) + fn(n, 2)) % 9901
    
print(answer)