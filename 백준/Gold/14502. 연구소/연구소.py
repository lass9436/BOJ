import sys
from collections import deque
R, C = map(int, sys.stdin.readline().split())

lab = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]

answer = []

def bfs():
    global lab, R, C, answer
    visited = [[False for col in range(C)] for row in range(R)]
    
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]] 
    
    queue = deque()
    
    labCopy = [[0 for col in range(C)] for row in range(R)]
    
    count = 0
    
    for i in range(R):
        for j in range(C):
            labCopy[i][j] = lab[i][j]
            
            if lab[i][j] == 2:
                queue.append([i, j])
                visited[i][j] = True
                
    while queue:
        cur = queue.popleft()
        r = cur[0]
        c = cur[1]
        
        for di in directions:
            dr = r + di[0]
            dc = c + di[1]
            if 0 <= dr < R and 0 <= dc < C and not visited[dr][dc] and labCopy[dr][dc] == 0:
                labCopy[dr][dc] = 2
                queue.append([dr, dc])
                visited[dr][dc] = True
                
    for i in range(R):
        for j in range(C):
            if labCopy[i][j] == 0:
                count += 1
                
    answer.append(count)

for i in range(R):
    for j in range(C):
        if lab[i][j] == 0:
            #벽을 세우다
            lab[i][j] = 1
            
            for k in range(i, R):
                for l in range(C):
                    if lab[k][l] == 0:
                        #두번째 벽을 세우다
                        lab[k][l] = 1
                        for m in range(k, R):
                            for n in range(C):
                                if lab[m][n] == 0:
                                    #세번째 벽을 세우다
                                    lab[m][n] = 1
                                    #bfs 시작
                                    bfs()
                                    #세번째 벽을 철거하다.
                                    lab[m][n] = 0
                        #두번째 벽을 철거하다
                        lab[k][l] = 0
            #세운 벽을 철거하다
            lab[i][j] = 0
            
print(max(answer))