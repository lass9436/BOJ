import sys
import heapq

heap = []

n = int(sys.stdin.readline())
count = 0

for i in range(n):
    heapq.heappush(heap, int(sys.stdin.readline()))

while heap:
    try:
        previous = heapq.heappop(heap)
        next = heapq.heappop(heap)
        sum = previous + next
        count += sum
        if not heap:
            break
        heapq.heappush(heap, sum)
    except:
        break
    
print(count)