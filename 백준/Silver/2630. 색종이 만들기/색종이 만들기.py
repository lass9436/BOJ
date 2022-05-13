import sys
sys.setrecursionlimit(10**7)

N = int(sys.stdin.readline())

paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

white = 0
blue = 0

def divide(r, c, n):
    global blue, white
    color = paper[r][c]
    for i in range(r, r+n):
        for j in range(c, c+n):
            if color != paper[i][j]:
                divide(r, c, int(n/2))
                divide(r, c + int(n/2), int(n/2))
                divide(r + int(n/2), c, int(n/2))
                divide(r + int(n/2), c + int(n/2), int(n/2))
                return
    if color == 0:
        white += 1
        return
    else:
        blue += 1
        return
    
divide(0,0,N)
print(white)
print(blue)