import sys
R, C, B = map(int, sys.stdin.readline().split())
area = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]
answer = sys.maxsize
height = 0

for hei in range(0, 257):
    addCount = 0
    removeCount = 0
    for r in range(0, R):
        for c in range(0, C):
            if hei - area[r][c] > 0:
                addCount += hei - area[r][c]
            else:
                removeCount += area[r][c] - hei
    if removeCount + B >= addCount:
        if answer >= (removeCount * 2 + addCount):
            answer = removeCount * 2 + addCount
            height = hei
            
print(answer, height)