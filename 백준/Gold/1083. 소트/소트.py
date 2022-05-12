import sys

n = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))

s = int(sys.stdin.readline())

while True:
    change = False
    for i in range(n):
        targetIdx = i
        for j in range(i+1, n):
            if (j - i) > s:
                break
            if arr[j] > arr[targetIdx]:
                targetIdx = j
        if targetIdx != i:
            change = True
            temp = arr[targetIdx]
            del arr[targetIdx]
            arr.insert(i, temp)
            s -= (targetIdx - i)
    if not change:
        break
        
print(" ".join(map(str, arr)))