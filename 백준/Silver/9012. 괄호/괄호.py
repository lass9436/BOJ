import sys
from collections import deque
N = int(sys.stdin.readline())
for _ in range(N):
    arr = deque(list(sys.stdin.readline().rstrip()))
    left = 0
    right = 0
    isPossible = True
    while arr:
        cur = arr.popleft()
        
        if cur == "(":
            left += 1
        else:
            right += 1
            
        if left < right:
            isPossible = False
        else:
            left -= right
            right = 0
    if isPossible and left == right == 0:
        print("YES")
    else:
        print("NO")