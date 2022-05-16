import math

S, E = map(int, input().split())

isPrime = [True for _ in range(E+1)]

if E >= 1:
    isPrime[0] = False
    isPrime[1] = False
    
for i in range(2, E+1):
    for j in range(2, int(math.sqrt(i)) + 1):
        if isPrime[j] and i % j == 0:
            isPrime[i] = False
            break

for i in range(S, E+1):
    if isPrime[i]:
        print(i)