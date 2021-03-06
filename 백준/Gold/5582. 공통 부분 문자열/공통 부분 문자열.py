import sys
str1 = " "+(sys.stdin.readline().rstrip())
str2 = " "+(sys.stdin.readline().rstrip())
dp = [[0 for _ in range(len(str2))] for _ in range(len(str1))]
answer = 0
for i in range(1, len(str1)):
    for j in range(1, len(str2)):
        if str1[i] == str2[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        answer = max(answer, dp[i][j])
print(answer)