import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

answer = 1
for i in arr:
    if answer < i:
        break
    answer += i
    
print(answer)