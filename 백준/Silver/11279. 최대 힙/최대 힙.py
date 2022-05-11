import sys
import heapq

n = int(input())
heap = []

for i in range(n):
    m = int(sys.stdin.readline())
    if m != 0:
        heapq.heappush(heap, (-m))
    else:
        try:
            print(-1 * heapq.heappop(heap))
        except:
            print(0)
        