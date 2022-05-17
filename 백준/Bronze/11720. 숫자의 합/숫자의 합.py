import sys

N = int(sys.stdin.readline())

arr = list(map(int, list(sys.stdin.readline().strip("\n"))))

answer = 0

for i in arr:
    answer += i
    
print(answer)