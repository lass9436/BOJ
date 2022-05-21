import sys
N = int(sys.stdin.readline())
dic = {}
arr = []
for _ in range(N):
    word = sys.stdin.readline().rstrip()
    if word not in dic:
        dic[word] = 1
        arr.append(word)
arr.sort(key=lambda x : (len(x), x))
for word in arr:
    print(word)