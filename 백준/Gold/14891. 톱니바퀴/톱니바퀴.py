import sys
wheels = [sys.stdin.readline().rstrip() for _ in range(4)]
base = [0] * 4

K = int(sys.stdin.readline())

def left(num):
    global base, wheels
    return wheels[num][(base[num] + 6)%8]

def right(num):
    global base, wheels
    return wheels[num][(base[num] + 2)%8]
    
def preLeft(num, clock):
    global base, wheels
    return wheels[num][(base[num] + clock + 6)%8]

def preRight(num, clock):
    global base, wheels
    return wheels[num][(base[num] + clock + 2)%8]

def rotate(num, clock, di):
    global base
    base[num] -= clock
    if di == 0:
        if num in [1,2,3] and preLeft(num, clock) != right(num-1):
            rotate(num-1, -clock, -1)
        if num in [0,1,2] and left(num+1) != preRight(num, clock):
            rotate(num+1, -clock, 1)
    if di == -1:
        if num in [1,2,3] and preLeft(num, clock) != right(num-1):
            rotate(num-1, -clock, -1)
    if di == 1:
        if num in [0,1,2] and left(num+1) != preRight(num, clock):
            rotate(num+1, -clock, 1)
            
def answer():
    global wheels, base
    ans = 0
    for i in range(4):
        ans += int(wheels[i][base[i]%8]) * (2 ** i)
    return ans
        
for _ in range(K):
    num, clock = map(int, sys.stdin.readline().split())
    rotate(num-1, clock, 0)
    
print(answer())