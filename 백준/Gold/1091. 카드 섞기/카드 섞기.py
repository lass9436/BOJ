import sys
sys.setrecursionlimit(10**7)
N = int(sys.stdin.readline())
P = list(map(int, sys.stdin.readline().split()))
S = list(map(int, sys.stdin.readline().split()))
origin = [0, 1, 2] * (N//3)
arr = [0, 1, 2] * (N//3)

def shuffle(depth):
    global arr
    if arr == P:
        print(depth)
        return
    elif depth != 0 and arr == origin:
        print(-1)
        return
    nextArr = [0] * N
    for i in range(N):
        nextArr[i] = arr[S[i]]
    arr = nextArr.copy()
    shuffle(depth+1)

shuffle(0)