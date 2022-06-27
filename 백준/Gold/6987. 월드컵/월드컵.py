import sys
ex1 = list(map(int, sys.stdin.readline().split()))
ex2 = list(map(int, sys.stdin.readline().split()))
ex3 = list(map(int, sys.stdin.readline().split()))
ex4 = list(map(int, sys.stdin.readline().split()))
answer = [0] * 4
result = [0] * 18

def gameResult(num1, num2, res, rev):
    global result
    #num1 가 num2 에게 res 했다.
    #rev 반전 여부
    if res == 0: # 승리
        if rev == 0:
            result[num1*3] += 1
            result[num2*3 + 2] += 1 
        else:
            result[num1*3] -= 1
            result[num2*3 + 2] -= 1 
    elif res == 1: #무승부
        if rev == 0:
            result[num1*3 + 1] += 1
            result[num2*3 + 1] += 1
        else:
            result[num1*3 + 1] -= 1
            result[num2*3 + 1] -= 1
    else: #패배
        if rev == 0:
            result[num1*3 + 2] += 1
            result[num2*3] += 1
        else:
            result[num1*3 + 2] -= 1
            result[num2*3] -= 1

def chk(depth):
    global result, ex1, ex2, ex3, ex4
    if result[0:depth*3] == ex1[0:depth*3]:
        return True
    if result[0:depth*3] == ex2[0:depth*3]:
        return True
    if result[0:depth*3] == ex3[0:depth*3]:
        return True
    if result[0:depth*3] == ex4[0:depth*3]:
        return True
    return False

def dfs(team1, team2):
    global result
    if team1 > 0 and not chk(team1):
        return
    if team2 == 6:
        dfs(team1+1, team1+2)
        return
    if team1 == 6:
        if answer[0] == 0 and result == ex1:
            answer[0] = 1
        if answer[1] == 0 and result == ex2:
            answer[1] = 1
        if answer[2] == 0 and result == ex3:
            answer[2] = 1
        if answer[3] == 0 and result == ex4:
            answer[3] = 1
        return
    for i in range(3):
        gameResult(team1, team2, i, 0)
        dfs(team1, team2 + 1)
        gameResult(team1, team2, i, -1)
dfs(0,1)
print(*answer)