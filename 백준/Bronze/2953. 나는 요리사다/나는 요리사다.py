arr = [list(map(int, input().split())) for _ in range(5)]
idx = 0
sum = 0
for i in range(5):
    s = 0
    for j in arr[i]:
        s = s + j
    if sum < s:
        idx = i
        sum = s
print(idx+1, sum)