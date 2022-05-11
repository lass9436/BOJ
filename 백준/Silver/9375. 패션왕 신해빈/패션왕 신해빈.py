import sys
line = sys.stdin.readline

n = int(line())

for i in range(n):
    dic = {}
    m = int(line())
    count = 1
    for j in range(m):
        what, fassion = line().split()
        if not fassion in dic:
            dic[fassion] = 1
        else:
            dic[fassion] += 1
    for k in dic.keys():
        count *= (dic[k] + 1)
    print(count-1)