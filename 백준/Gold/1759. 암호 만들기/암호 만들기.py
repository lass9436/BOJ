import sys
#L은 문자열의 길이, C는 문자 후보의 개수
L, C = map(int, sys.stdin.readline().split())
arr = sys.stdin.readline().split()
arr.sort()

password = []

def check(password):
    
    vowel = ["a", "e", "i", "o", "u"]
    #모음 개수
    vowelCnt = 0
    
    for i in password:
        if i in vowel:
            vowelCnt +=1
    #자음 개수
    conCnt = len(password) - vowelCnt
    if vowelCnt >= 1 and conCnt >= 2:
        return True
    return False

def brute(depth):
    
    global L, C, arr, password
    
    if depth == L:
        if check(password):
            print("".join(password))
        
    for i in arr:
        if not i in password:
            if not password:
                password.append(i)
                brute(depth+1)
                password.pop()
            elif password and password[-1] < i:
                password.append(i)
                brute(depth+1)
                password.pop()
            
brute(0)