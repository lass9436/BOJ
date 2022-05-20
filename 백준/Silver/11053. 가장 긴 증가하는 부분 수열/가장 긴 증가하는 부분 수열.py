import sys

N = int(sys.stdin.readline())
arr = [0]

for i in list(map(int, sys.stdin.readline().split())):
    arr.append(i)
    
dp = [0] * (N+1)

for i in range(1, N+1):
    for j in range(0, i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)

answer = 0

for i in dp:
    if answer < i:
        answer = i

print(answer)