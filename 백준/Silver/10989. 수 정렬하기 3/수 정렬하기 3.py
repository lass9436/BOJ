import sys

N = int(sys.stdin.readline())

arr = [0 for _ in range(10001)]

for i in range(N):
    num = int(sys.stdin.readline())
    arr[num] += 1
    
for i in range(10001):
    for j in range(arr[i]):
        print(i)