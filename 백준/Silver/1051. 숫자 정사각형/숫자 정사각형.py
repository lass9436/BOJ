import sys
N, M = map(int ,sys.stdin.readline().split(" "))
arr = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(N)];
l = min(N, M)
answer = 0
for i in range(N):
    for j in range(M):
        for k in range(l):
            if ((i + k) < N) and ((j + k) < M) and (arr[i][j] == arr[i][j + k] == arr[i + k][j] == arr[i + k][j + k]):
                answer = max(answer, (k + 1)**2)
print(answer)