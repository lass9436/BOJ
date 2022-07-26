import sys
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split(" ")))
arr.sort()
answer = 0
for i in range(len(arr)):
    answer += sum(arr[0:i+1])
print(answer)