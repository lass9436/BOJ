import sys

n = int(sys.stdin.readline())

meet = []

for i in range(n):
    start, end = map(int, sys.stdin.readline().split())
    meet.append([start, end])
    
meet.sort(key=lambda x: (x[1], x[0]))

answer = 0
endTime = 0

for i in range(len(meet)):
    if endTime <= meet[i][0]:
        endTime = meet[i][1]
        answer += 1
        
print(answer)