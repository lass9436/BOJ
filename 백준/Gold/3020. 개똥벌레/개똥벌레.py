import sys
from bisect import bisect_left, bisect_right

N, H = map(int, sys.stdin.readline().split())

bottoms = []
tops = []

for i in range(N//2):
    bottom = int(sys.stdin.readline())
    top = int(sys.stdin.readline())
    
    bottoms.append(bottom)
    tops.append(top)
    
bottoms.sort()
tops.sort()

countMin = -1
countHeight = 0

def breakBottoms(height):
    global bottoms
    return len(bottoms) - bisect_left(bottoms, height)

def breakTops(height):
    global tops, H
    return len(tops) - bisect_left(tops, H - height + 1)

for i in range(1, H+1):
    bot = breakBottoms(i)
    top = breakTops(i)
    n = bot + top
    
    if countMin == -1:
        countMin = n
        
    if countMin > n:
        countMin = n
        countHeight = 1
    elif countMin == n:
        countHeight += 1
        
print(countMin, countHeight)