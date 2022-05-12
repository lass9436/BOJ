import sys
plus = sys.stdin.readline().split("-")

answer = 0

count = 0
for i in plus:
    eq = list(map(int, i.split("+")))
    for j in eq:
        if count == 0:
            answer += j
        else:
            answer -= j
    count += 1
    
print(answer)
            
    
        