from collections import deque
import sys
N, K = map(int, sys.stdin.readline().split())
belt = deque(list(map(int, sys.stdin.readline().split())))
robot = deque([0]*(2*N))
answer = 0

def chk():
    global belt, K
    count = 0
    for i in belt:
        if i == 0:
            count += 1
    if count >= K:
        return False
    return True

def move():
    global belt, robot, N
    for i in range(2*N-1, -1, -1):
        if robot[i] == 1:
            if robot[i+1] == 0 and belt[i+1] > 0:
                robot[i] = 0
                robot[i+1] = 1
                belt[i+1] -= 1
                
def unload():
    global robot
    if robot[N-1] == 1:
        robot[N-1] = 0

while chk():
    answer += 1
    belt.rotate()
    robot.rotate()
    unload()
    move()
    unload()
    if belt[0] > 0:
        robot[0] = 1
        belt[0] -= 1
    unload()
print(answer)