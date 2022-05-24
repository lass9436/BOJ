import sys, math
N = int(sys.stdin.readline())
for _ in range(N):
    A, B = map(int, sys.stdin.readline().split())
    distance = B - A
    maxc = int(math.sqrt(distance))
    
    if maxc == math.sqrt(distance):
        print(maxc * 2 - 1)
    elif distance <= maxc * maxc + maxc:
        print(maxc * 2)
    else:
        print(maxc * 2 + 1)