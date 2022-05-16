import sys

N, M = map(int, sys.stdin.readline().split())

arr = []

for i in range(N):
    arr.append(int(sys.stdin.readline()))
    
arr.sort()

start = 1
end = max(arr)
answer = 0

while start <= end:
    count = 0
    find = (start + end) // 2
    for i in arr:
        count += i // find
    if count >= M:
        start = find + 1
        if answer < find:
            answer = find
    else:
        end = find - 1
print(answer)        