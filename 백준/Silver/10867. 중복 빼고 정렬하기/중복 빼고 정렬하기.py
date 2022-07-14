import sys
N = int(sys.stdin.readline())
arr = list(set(list(map(int, sys.stdin.readline().split()))))
arr.sort()
print(*arr)