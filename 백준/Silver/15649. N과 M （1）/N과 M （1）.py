N, M = map(int, input().split())

arr = []

def search(depth):
    if depth == M:
        print(" ".join(map(str, arr)))
        return
    for i in range(1, N+1):
        if not i in arr:
            arr.append(i)
            search(depth+1)
            arr.pop()
        
search(0)