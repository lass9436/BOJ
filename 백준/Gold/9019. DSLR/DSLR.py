import sys
from collections import deque
N = int(sys.stdin.readline())
for _ in range(N):
    A, B = map(int, sys.stdin.readline().split())
    visited = [False] * 10000
    queue = deque()
    queue.append((A, ""))
    while queue:
        C, order = queue.popleft()
        d1 = C//1000
        d2 = C%1000//100
        d3 = C%100//10
        d4 = C%10
        if B == C:
            print(order)
            break
        if visited[C]:
            continue
        visited[C] = True
        queue.append(((2*C)%10000, order + "D"))
        queue.append((9999 if C == 0 else C-1, order + "S"))
        queue.append((d2*1000 + d3*100 + d4*10 + d1 , order + "L"))
        queue.append((d4*1000 + d1*100 + d2*10 + d3, order + "R"))
        