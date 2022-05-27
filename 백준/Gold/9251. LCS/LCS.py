import sys
arr1 = list("." + sys.stdin.readline().rstrip())
arr2 = list("." + sys.stdin.readline().rstrip())
dp = [[0 for _ in range(len(arr2))] for _ in range(len(arr1))]

for i in range(1, len(arr1)):
    for j in range(1, len(arr2)):
        if arr1[i] == arr2[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[len(arr1)-1][len(arr2)-1])