import sys
N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
dis = []
for i in range(1, N):
    dis.append(arr[i] - arr[i-1])
dis.sort()
for i in range(1, K):
    if dis:
        dis.pop()
print(sum(dis) if dis else 0)