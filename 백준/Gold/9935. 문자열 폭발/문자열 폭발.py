import sys
from collections import deque

line = str(sys.stdin.readline().strip())
bomb = str(sys.stdin.readline().strip())

l = deque()

for i in line:
    l.append(i)
    if len(l) >= len(bomb):
        tof = True
        for idx in range(1, len(bomb)+1):
            if l[-idx] != bomb[-idx]:
                tof = False
                break
        if tof:
            for j in range(len(bomb)):
                l.pop()

if len(l) == 0:
    print("FRULA")
else:
    print("".join(l))
