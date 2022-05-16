import sys
from bisect import bisect_left, bisect_right

N = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())

find = list(map(int, sys.stdin.readline().split()))

arr.sort()

for i in find:
    if bisect_left(arr, i) != bisect_right(arr, i):
        print(1)
    else:
        print(0)
