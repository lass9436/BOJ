import sys
N, M = map(int, sys.stdin.readline().split())
times = [int(sys.stdin.readline()) for _ in range(N)]
start = min(times)
end = max(times) * M

while start <= end:
    num = 0
    mid = (start + end)//2
    for time in times:
        num += mid // time
    if num >= M:
        end = mid - 1
    else:
        start = mid + 1

print(start)