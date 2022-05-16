import sys

N = int(sys.stdin.readline())

for i in range(N):
    A, B = map(int, sys.stdin.readline().split())
    a, b = max(A, B), min(A, B)
    while a % b != 0:
        a, b = b, a % b
    GCD = b
    print(A * B // b)