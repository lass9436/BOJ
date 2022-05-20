import sys
line = sys.stdin.readline().upper().strip()

count = 0
initial = ""
dic = {}

for i in line:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] = dic[i] + 1

for i in dic:
    if dic[i] > count:
        count = dic[i]
        initial = i
    elif dic[i] == count:
        initial = "?"

print(initial)        