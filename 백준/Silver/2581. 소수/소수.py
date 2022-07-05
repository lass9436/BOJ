import sys
S = int(sys.stdin.readline())
E = int(sys.stdin.readline())
arr = []
for i in range(S, E+1):
    isPrime = True
    if i == 1 or i == 0:
        isPrime = False
    for j in range(2, int(i**(1/2))+1):
        if i % j == 0:
            isPrime = False
            break
    if isPrime:
        arr.append(i)
if arr:
    print(sum(arr))
    print(arr[0])
else:
    print(-1)