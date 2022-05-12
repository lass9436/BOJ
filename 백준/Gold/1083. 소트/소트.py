import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
s = int(sys.stdin.readline())

for i in range(n):
    targetIdx = i
    for j in range(i+1, n):
        if (j - i) > s:
            break
        if arr[j] > arr[targetIdx]:
            targetIdx = j
    if targetIdx != i:
        temp = arr[targetIdx]
        del arr[targetIdx]
        arr.insert(i, temp)
        s -= (targetIdx - i)
        
print(" ".join(map(str, arr)))