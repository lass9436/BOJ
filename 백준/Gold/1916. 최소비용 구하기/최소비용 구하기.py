import sys, heapq
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
adj = [[] for _ in range(N+1)]
for _ in range(M):
    u, v, w = map(int, sys.stdin.readline().split())
    adj[u].append((w, v))
dist = [sys.maxsize] * (N+1)
S, E = map(int, sys.stdin.readline().split())

heap = []
heapq.heappush(heap, (0, S))

while heap:
    w, node = heapq.heappop(heap)
    if w < dist[node]:
        dist[node] = w
        for weight, nextNode in adj[node]:
            heapq.heappush(heap, (weight + w, nextNode))
            
print(dist[E])