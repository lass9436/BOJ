import sys
N = int(sys.stdin.readline())

def isPrime(i):
    if i == 1:
        return False
    for j in range(2, i):
        if i % j == 0:
            return False
    return True        
numbers = []
def dfs(depth):
    global numbers
    if depth == N:
        print("".join(map(str, numbers)))
        return
    for i in range(1, 10):
        numbers.append(i)
        if isPrime(int("".join(map(str, numbers)))):
            dfs(depth + 1)
        numbers.pop()
        
dfs(0)