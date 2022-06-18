import sys, heapq

N = int(sys.stdin.readline())
adj = [[] for _ in range(N+1)]
time = [0] * (N+1)
degree = [0] * (N+1)
answer = 0
visited = [False] * (N+1)
for i in range(1, N+1):
    arr = list(map(int, sys.stdin.readline().split()))
    time[i] = arr[0]
    for j in range(arr[1]):
        adj[arr[2+j]].append(i)
        degree[i] += 1
heap = []
for i in range(1, N+1):
    if degree[i] == 0:
        heapq.heappush(heap, (time[i], i))
        visited[i] = True
while heap:
    curTime, curNode = heapq.heappop(heap)
    answer = max(answer, curTime)
    for i in adj[curNode]:
        degree[i] -= 1
    for i in range(1, N+1):
        if degree[i] == 0 and not visited[i]:            
            heapq.heappush(heap, (curTime + time[i], i))
            visited[i] = True
print(answer)