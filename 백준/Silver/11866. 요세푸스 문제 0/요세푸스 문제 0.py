import sys
from collections import deque
N, K = map(int, sys.stdin.readline().split())
q = deque([i for i in range(1, N+1)])
arr = []

count = 0
while q:
    cur = q.popleft()
    count += 1
    if count == K:
        count = 0
        arr.append(cur)
    else:
        q.append(cur)
        
print("<", end="")

for i in range(len(arr)):
    if i != 0:
        print(", ", end="")
    print(arr[i], end="")
    
print(">")