import sys
from collections import deque
N, K = map(int, sys.stdin.readline().split())
visited = [False] * (100002)
queue = deque()
answer = 0

queue.append((N, 0))

while queue:

    position, time = queue.popleft()
    if position > 100001:
        continue
    if visited[position]:
        continue
    visited[position] = True
    if position == K:
        answer = time
        break
    if position > 0:
        queue.appendleft((2 * position, time))
        queue.append((position - 1, time + 1))
    queue.append((position + 1, time + 1))        

print(answer)