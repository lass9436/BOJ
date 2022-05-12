import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

while True:
    change = False
    for i in range(n-1):
        if arr[i] + 1 == arr[i+1]:
            change = True
            cha = False
            for j in range(i+1, n):
                if arr[i+1] < arr[j]:
                    arr[i+1], arr[j] = arr[j], arr[i+1]
                    cha = True
                    break
            if not cha:
                arr[i], arr[i+1] = arr[i+1], arr[i]
    if not change:
        break

print(" ".join(map(str, arr)))