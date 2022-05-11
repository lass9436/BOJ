import sys
import heapq

n = int(sys.stdin.readline())

card = [int(sys.stdin.readline()) for _ in range(n)]
heapq.heapify(card)
count = 0

while len(card) != 1:
    first = heapq.heappop(card)
    second = heapq.heappop(card)
    sum = first + second
    count += sum
    heapq.heappush(card, sum)
    
print(count)