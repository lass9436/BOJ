import sys

N = int(sys.stdin.readline())

chess = [[0 for c in range(N)] for r in range(N)]

row = [0] * N
col = [0] * N
diaRight = [0] * (2*N)
diaLeft = [0] * (2*N)

def check(r, c):
    global row, col, diaRight, diaLeft, N
    if row[r] > 0:
        return False
    if col[c] > 0:
        return False
    if diaRight[r+c] > 0:
        return False
    if diaLeft[r-c+N] > 0:
        return False
    return True

def inQueen(r, c):
    global row, col, diaRight, diaLeft, N
    row[r] += 1
    col[c] += 1
    diaRight[r+c] += 1
    diaLeft[r-c+N] += 1
    
def outQueen(r, c):
    global row, col, diaRight, diaLeft, N
    row[r] -= 1
    col[c] -= 1
    diaRight[r+c] -= 1
    diaLeft[r-c+N] -= 1

def queen(depth):
    global N, chess
    count = 0
    if depth == N:
        return 1
    for i in range(N):
        if check(depth, i):
            inQueen(depth, i)
            chess[depth][i] = 1
            count += queen(depth+1)
            chess[depth][i] = 0
            outQueen(depth, i)
    return count

print(queen(0))