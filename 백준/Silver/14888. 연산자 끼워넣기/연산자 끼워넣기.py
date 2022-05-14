import sys

N = int(sys.stdin.readline())

nums = list(map(int, sys.stdin.readline().split()))

opes = list(map(int, sys.stdin.readline().split()))

arr = []
answer = []

def operation():
    global arr
    global nums
    
    num = nums[0]
    count = 1
    for i in arr:
        if i == '+':
            num = num + nums[count]
        if i == '-':
            num = num - nums[count]
        if i == '*':
            num = num * nums[count]
        if i == '/':
            num = int(num / nums[count])
        count += 1
    return num

def backtrack(depth):
    global opes
    
    if depth + 1 == N:
        answer.append(operation())
        return
        
    if opes[0] > 0:
        opes[0] -= 1
        arr.append('+')
        backtrack(depth+1)
        arr.pop()
        opes[0] += 1
    if opes[1] > 0:
        opes[1] -= 1
        arr.append('-')
        backtrack(depth+1)
        arr.pop()
        opes[1] += 1
    if opes[2] > 0:
        opes[2] -= 1
        arr.append('*')
        backtrack(depth+1)
        arr.pop()
        opes[2] += 1
    if opes[3] > 0:
        opes[3] -= 1
        arr.append('/')
        backtrack(depth+1)
        arr.pop()
        opes[3] += 1        
        
backtrack(0)

print(max(answer))
print(min(answer))