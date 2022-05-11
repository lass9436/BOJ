import sys
sys.setrecursionlimit(10**7)

n = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(n)]
dp = [-1 * n for _ in range(n)]

if n > 0:
    dp[0] = arr[0]
if n > 1:
    dp[1] = arr[0] + arr[1] 

def f (n):
    if dp[n] > -1:
        return dp[n]
    dp[n] = max(fn(n, 0), fn(n, 1), fn(n, 2))
    return dp[n]

def fn (n, k):
    if n < 0:
        return 0
    if n == 0 and k == 0:
        return 0
    if n == 0 and k >= 1:
        return arr[0]
    return max(f(n-1), (f(n-2) + arr[n]), (f(n-3) + arr[n] + arr[n-1]))

print(f(n-1))