import sys
N = int(sys.stdin.readline())
count = 0
for _ in range(N):
    dic = dict()
    word = sys.stdin.readline().rstrip()
    group = True
    for i in range(len(word)-1):
        if word[i] == word[i+1]:
            continue
        else:
            if not word[i] in dic:
                dic[word[i]] = 1
            else:
                group = False
                break
    if word[-1] in dic:
        group = False
    if group:
        count += 1
print(count)