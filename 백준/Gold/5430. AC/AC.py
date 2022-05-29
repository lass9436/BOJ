import sys
from collections import deque
N = int(sys.stdin.readline())

for _ in range(N):
    
    order = list(sys.stdin.readline().rstrip())
    l = int(sys.stdin.readline())
    string = sys.stdin.readline().rstrip()
    string = string[1:-1]
    arr = deque(string.split(","))
    if l == 0:
        arr = []
            
    isError = False
    
    rCount = 0
           
    isReverse = False
    
    for i in order:
        if i == "R":
            rCount += 1
            isReverse = not isReverse
        elif i == "D" and not arr:
            isError = True
            print("error")
            break
        elif i == "D" and not isReverse:
            arr.popleft()
        elif i == "D" and isReverse:
            arr.pop()
            
    if rCount%2==1:
        arr.reverse()
    
    if not isError:
        print("[" + ",".join(arr) + "]")