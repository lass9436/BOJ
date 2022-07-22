import sys
N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    temp = sys.stdin.readline().split()
    arr.append(temp)
arr.sort(key=lambda x : (int(x[3]), int(x[2]), int(x[1])));
print(arr[-1][0])
print(arr[0][0])