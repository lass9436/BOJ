N, M = map(int, input().split(":"))

a, b = max(N, M), min(N, M)

while a % b != 0:
    a, b = b, a % b

print(":".join(map(str, [N//b, M//b])))