import sys
from collections import deque
N = int(sys.stdin.readline())
arr = [i for i in range(1, N+1)]
q = deque(arr)
answer = []
while q:
    answer.append(q.popleft())
    if q:
        q.append(q.popleft())
print(*answer)