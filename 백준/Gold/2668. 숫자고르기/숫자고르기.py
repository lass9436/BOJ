import sys
sys.setrecursionlimit(10**7)
N = int(sys.stdin.readline())
adj = [[] for _ in range(N+1)]
answer = set()

for i in range(1, N+1):
    adj[i].append(int(sys.stdin.readline()))

visited = [False for _ in range(N+1)]
    
def dfs(number):
    global adj
    if visited[number]:
        if number in answer:
            return
        answer.add(number)
    visited[number] = True
    for i in adj[number]:
        dfs(i)

for i in range(1, N+1):
    visited = [False for _ in range(N+1)]
    dfs(i)
    
answer = list(answer)
answer.sort()
print(len(answer))
for i in answer:
    print(i)