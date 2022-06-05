import sys
N = int(sys.stdin.readline())
dpMax = [0] * 3
dpMin = [0] * 3
tempMax = [0] * 3
tempMin = [0] * 3
for i in range(1, N+1):
    a, b, c = map(int, sys.stdin.readline().split())
    for j in range(3):
        if j == 0:
            tempMax[j] = a + max(dpMax[0], dpMax[1])
            tempMin[j] = a + min(dpMin[0], dpMin[1])
        if j == 1:            
            tempMax[j] = b + max(dpMax[0], dpMax[1], dpMax[2])
            tempMin[j] = b + min(dpMin[0], dpMin[1], dpMin[2])
        if j == 2:
            tempMax[j] = c + max(dpMax[1], dpMax[2])
            tempMin[j] = c + min(dpMin[1], dpMin[2])
    dpMax = tempMax.copy()
    dpMin = tempMin.copy()
print(max(dpMax), min(dpMin))