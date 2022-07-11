S = int(input())
n = 1
while True:
    s = n * (n + 1) / 2
    if S == s:
        break
    elif S < s:
        n -= 1
        break
    n += 1
print(n)