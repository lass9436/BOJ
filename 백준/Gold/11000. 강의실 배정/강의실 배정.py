import sys, heapq
N = int(sys.stdin.readline())
arr = []
answer = 0
for _ in range(N):
    a = tuple(map(int, sys.stdin.readline().split()))
    arr.append(a)
arr.sort()
heap = []
for i in arr:
    a, b = i
    while heap and heap[0][0] <= i[0]:
        heapq.heappop(heap)
    heapq.heappush(heap, (b, a))
    answer = max(answer, len(heap))
print(answer)