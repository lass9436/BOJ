import sys
target = int(sys.stdin.readline())
N = int(sys.stdin.readline())
breakButtons = list(map(int, sys.stdin.readline().split()))
cur = 100
answer = abs(target - 100)

for i in range(0, 1000001):
    isImpossible = False
    
    for j in str(i):
        if int(j) in breakButtons:
            isImpossible = True
            break
    
    if isImpossible:
        continue
        
    dist = abs(target - i) + len(str(i))
    if answer > dist:
        answer = dist

print(answer)