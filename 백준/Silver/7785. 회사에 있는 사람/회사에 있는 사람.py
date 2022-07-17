import sys
N = int(sys.stdin.readline())
dic = {}
for _ in range(N):
    arr = sys.stdin.readline().split()
    if arr[1] == "enter":
        dic[arr[0]] = True
    elif arr[1] == "leave":
        dic[arr[0]] = False
arr = []
for key in dic:
    if dic[key]:
        arr.append(key)
arr.sort(reverse=True)
for i in arr:
    print(i)