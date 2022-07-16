import sys
arr = [(int(sys.stdin.readline()), i+1) for i in range(8)]
arr.sort(key = lambda x : (-x[0], x[1]))
answer = 0
for i in range(5):
    answer += arr[i][0]
print(answer)
arr2 = []
for i in range(5):
    arr2.append(arr[i][1])
arr2.sort()
print(*arr2)