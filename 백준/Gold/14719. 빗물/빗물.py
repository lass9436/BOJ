import sys
R, C = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
answer = 0
for i in range(0, R):
    left = -1
    right = -1
    for j in range(0, C):
        height = arr[j]
        if height > i:
            if left == right == -1:
                left = j
            elif left >= right:
                right = j
                answer += right - left - 1
                left = j
print(answer)