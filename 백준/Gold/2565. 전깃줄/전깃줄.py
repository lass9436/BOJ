import sys
N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
arr.insert(0, [0, 0])
arr.sort()
dp = [0] * (N+1)

for i in range(1, N+1):
    for j in range(0, i):
        if arr[i][1] > arr[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)
            
print(N - max(dp))