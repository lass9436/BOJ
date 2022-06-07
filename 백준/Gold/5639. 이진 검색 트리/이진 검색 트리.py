import sys
sys.setrecursionlimit(10**7)
arr = []

while True:
    try:
        arr.append(int(sys.stdin.readline()))
    except:
        break

N = len(arr)
        
def dfs(start, end):
    global arr
    
    if start >= end:
        return
    
    cri = arr[start]
    
    start = start + 1
    
    right = start
    
    for i in range(start, end):
        if arr[i] > cri:
            right = i   
            break
            
    dfs(start, right)
    dfs(right, end)
    print(cri)
    
dfs(0, N)