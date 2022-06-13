import sys
T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    coins = list(map(int, sys.stdin.readline().split()))
    money = int(sys.stdin.readline())
    dp = [0] * (money + 1)
    for coin in coins:
        for i in range(1, money + 1):
            if i == coin:
                dp[i] += 1
            elif i > coin:
                dp[i] += dp[i - coin]
    print(dp[money])                