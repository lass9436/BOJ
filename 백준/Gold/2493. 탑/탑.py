import sys
from collections import deque
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
answer = [0] * (N)
queue = deque()

for i in range(N):
    while queue and queue[-1][1] < arr[i]:
        index, height = queue.pop()
        if queue:
            targetIndex, targetHeight = queue[-1]
            answer[index] = targetIndex + 1
    if queue:
        index, height = queue[-1]
        answer[i] = index + 1        
    queue.append((i, arr[i]))
    
print(*answer)