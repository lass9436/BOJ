import sys
plus = sys.stdin.readline().split("-")

answer = 0

for i in plus[0].split("+"):
    answer += int(i)

for i in plus[1:]:
    for j in i.split("+"):
        answer -= int(j)
        
print(answer)