N, M = map(int, input().split())

def search(seq, depth):
    global N, M
    if depth == M:
        print(" ".join(seq))
        return
    for i in range(1, N+1):
        search(seq + str(i), depth+1)
        
search("", 0)