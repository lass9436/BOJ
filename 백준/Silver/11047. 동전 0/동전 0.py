import sys
N, K = map(int, sys.stdin.readline().split()) 
coins = []
for i in range(N):
    coins.append(int(sys.stdin.readline()))

count = 0
for i in reversed(range(N)):
    count += K//coins[i]
    K = K%coins[i]
    
print(count)