import sys
N = int(sys.stdin.readline())
S = 0b000000000000000000000
for _ in range(N):
    temp = sys.stdin.readline().split()
    order = ""
    number = 0
    
    if len(temp) == 1:
        order = temp[0]
    else:
        order = temp[0]
        number = int(temp[1])
        
    if order == "add":
        S |= 1<<number
    elif order == "check":
        print(1 if S & 1<<number != 0 else 0)
    elif order == "remove":
        S &= ~(1<<number)
    elif order == "toggle":
        S ^= 1<<number
    elif order == "all":
        S = (1<<21)-1
    elif order == "empty":
        S = 0