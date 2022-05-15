import sys

N, S = map(int, sys.stdin.readline().split())

nums = list(map(int, sys.stdin.readline().split()))
answer = 0
arr = []

def dfs(depth):
    
    global nums, S, N, answer, arr
    
    if depth == N:
        if arr and sum(arr) == S:
            answer += 1
        return
    
    dfs(depth + 1)
    arr.append(nums[depth])
    dfs(depth + 1)
    arr.pop()

dfs(0)
print(answer)