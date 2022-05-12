import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

existA = [int(0) for _ in range(1001)]
existB = [int(0) for _ in range(1001)]

for a in A:
    existA[a] += 1
    
for b in B:
    existB[b] += 1

answer = 0
    
for i in range(1001):
    while existA[i] > 0:
        battle = False
        for j in range(i-1, 0, -1):
            if existB[j] > 0:
                battle = True
                answer += 2
                existA[i] -= 1
                existB[j] -= 1
                break
        if not battle:
            break
                
for i in range(1001):
    while existA[i] and existB[i]:
        existA[i] -= 1
        existB[i] -= 1
        answer += 1

print(answer)