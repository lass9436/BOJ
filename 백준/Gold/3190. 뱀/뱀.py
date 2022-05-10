from collections import deque

def change_direction (current_di, command):
    if command == 'L':
        current_di = (current_di - 1) % 4
    else:
        current_di = (current_di + 1) % 4
    return current_di

N = int(input())
board = [[0] * N for _ in range(N)]

apples = int(input())

for i in range(apples):
    row, col = map(int, input().split())
    board[row - 1][col - 1] = 1
    
c_count = int(input())
commands = {}

for i in range(c_count):
    time, command = input().split()
    commands[int(time)] = command

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

time = 1
direction = 0
r, c = 0, 0
snake = deque([[r, c]])
board[r][c] = 2

while True:
    r, c = r + dr[direction], c + dc[direction]
    if not (0 <= r < N and 0 <= c < N):
        break
    if board[r][c] == 2:
        break
    if board[r][c] == 1:
        snake.append([r,c])
        board[r][c] = 2
    if board[r][c] == 0:
        snake.append([r,c])
        board[r][c] = 2
        y, x = snake.popleft()
        board[y][x] = 0
    if time in commands.keys():
        direction = change_direction(direction, commands[time])
    time += 1
                
print(time)