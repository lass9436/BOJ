import sys
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

res = sys.maxsize
answer = [0] * 2
left = 0
right = N - 1 

while left < right:
    a = arr[left]
    b = arr[right]
    result = a + b
    if result > 0:
        right = right - 1
    else:
        left = left + 1
    if abs(result) < res:
        res = abs(result)
        answer[0] = a
        answer[1] = b
        
print(*answer)