import sys
N = int(sys.stdin.readline())
words = []
base36 = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
arr = []
answer = 0

def count(word):
    cnt = 0
    for i in range(len(word)):
        char = word[-1-i]
        dec = base36.index(char)
        cnt += dec * (36**i)
    return cnt

def to_36(cnt):
    a, b = cnt // 36, cnt % 36
    last = base36[b]
    return to_36(a) + last if a != 0 else last
    
for _ in range(N):
    words.append(sys.stdin.readline().rstrip())
    
K = int(sys.stdin.readline())

for i in base36:
    cnt = 0
    for word in words:
        change_word = word.replace(i, "Z")
        cnt += count(change_word)
    arr.append((cnt, i))

arr.sort(key = lambda x : -x[0])

for word in words:
    for i in range(K):
        word = word.replace(arr[i][1], "Z")
    answer += count(word)
    
print(to_36(answer))