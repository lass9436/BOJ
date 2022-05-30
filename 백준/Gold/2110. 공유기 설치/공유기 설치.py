import sys

N, M = map(int, sys.stdin.readline().split())
arr = [int(sys.stdin.readline()) for _ in range(N)]
arr.sort()

def binary_search(start, end):
    global arr, M
    while start <= end:
        count = 1
        mid = (start + end) // 2
        pre = arr[0]
        for i in arr:
            if i - pre >= mid:
                pre = i
                count += 1
        if count >= M:
            start = mid+1
        else:
            end = mid-1
    return start - 1

print(binary_search(1, arr[-1]))