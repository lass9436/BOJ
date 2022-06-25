import sys
N = int(sys.stdin.readline())
cranes = list(map(int, sys.stdin.readline().split()))
cranes.sort(reverse=True)
M = int(sys.stdin.readline())
boxes = list(map(int, sys.stdin.readline().split()))
boxes.sort(reverse=True)

answer = 0

while boxes:
    l = len(boxes)
    for crane in cranes:
        for box in boxes:
            if box <= crane:
                boxes.remove(box)
                break
    if l == len(boxes):
        print(-1)
        exit()
    answer += 1

print(answer)