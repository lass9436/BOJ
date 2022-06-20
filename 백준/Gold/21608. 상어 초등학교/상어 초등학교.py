import sys
N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N**2)]
area = [[0 for _ in range(N)] for _ in range(N)]
move = [[1, 0], [-1, 0], [0, 1], [0, -1]]

def findSeat(idx):
    global arr, N, area
    friends = arr[idx][1:]
    maxCount = 0
    maxEmpty = 0
    r = c = -1
    for i in range(N):
        for j in range(N):
            if area[i][j] > 0:
                continue
            if r == c == -1:
                r = i
                c = j
            count, empty = findFriends(i, j, friends)
            if count > maxCount:
                maxCount = count
                maxEmpty = empty
                r = i
                c = j
            elif count == maxCount and empty > maxEmpty:
                maxEmpty = empty
                r = i
                c = j
    return (r, c)

def findFriends(i, j, friends):
    global area, N, move
    count = 0
    empty = 0
    for k in range(4):
        dr = i + move[k][0]
        dc = j + move[k][1]
        if 0 <= dr < N and 0 <= dc < N:
            if area[dr][dc] in friends:
                count += 1
            elif area[dr][dc] == 0:
                empty += 1  
    return (count, empty)

for i in range(N**2):
    r, c = findSeat(i)
    area[r][c] = arr[i][0]
    
def findSatisfaction(i, j):
    global area, arr, move
    num = area[i][j]
    friends = []
    count = 0
    for k in range(N**2):
        if num == arr[k][0]:
            friends = arr[k][1:]
    for k in range(4):
        dr = i + move[k][0]
        dc = j + move[k][1]
        if 0 <= dr < N and 0 <= dc < N:
            if area[dr][dc] in friends:
                count += 1
    if count == 0:
        return 0
    else:
        return 10**(count-1)
    
answer = 0

for i in range(N):
    for j in range(N):
        answer += findSatisfaction(i, j)

print(answer)