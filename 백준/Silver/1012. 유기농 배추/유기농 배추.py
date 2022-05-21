import sys
from collections import deque
N = int(sys.stdin.readline())

move = [[1,0], [-1,0], [0,1], [0,-1]]

for _ in range(N):
    R, C, K = map(int, sys.stdin.readline().split())
    world = [[0 for _ in range(C)] for _ in range(R)]
    for _ in range(K):
        r, c = map(int, sys.stdin.readline().split())
        world[r][c] = 1
    visited = [[False for _ in range(C)] for _ in range(R)]
    queue = deque()
    
    count = 0
    
    for i in range(R):
        for j in range(C):
            if not visited[i][j] and world[i][j] == 1:
                visited[i][j] = True                
                count += 1
                queue.append([i,j])
                while queue:
                    cur = queue.popleft()
                    r = cur[0]
                    c = cur[1]
                    for k in range(4):
                        dr = r + move[k][0]
                        dc = c + move[k][1]
                        if 0 <= dr < R and 0<= dc < C and not visited[dr][dc] and world[dr][dc] == 1:
                            visited[dr][dc] = True
                            queue.append([dr, dc])
    
    print(count)