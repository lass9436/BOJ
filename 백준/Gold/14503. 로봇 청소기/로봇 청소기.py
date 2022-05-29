import sys
R, C = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())
area = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]
move = [[-1, 0], [0, 1], [1, 0], [0, -1]]
answer = 0

def rotate(d):
    return (d-1)%4

def nextPosition(r, c, d):
    global move
    dr = r + move[d][0]
    dc = c + move[d][1]
    return (dr, dc)

def backPosition(r, c, d):
    global move
    dr = r - move[d][0]
    dc = c - move[d][1]
    return (dr, dc)

def clean(r, c):
    global area, answer
    if area[r][c] == 0:
        area[r][c] = 2
        answer += 1

end = False
while True:
    if end:
        break
    clean(r, c)
    for i in range(4):
        d = rotate(d)
        dr, dc = nextPosition(r, c, d)
        if area[dr][dc] == 0:
            r, c = dr, dc
            break
        if i == 3:
            dr, dc = backPosition(r, c, d)
            if area[dr][dc] == 1:
                end = True
                break
            else:
                r, c = dr, dc
print(answer)