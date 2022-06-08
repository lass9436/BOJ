import re
import sys
 
T = int(sys.stdin.readline())
p = re.compile('(100+1+|01)+')
 
for _ in range(T):
    sign = sys.stdin.readline().rstrip()
    m = p.fullmatch(sign)
    if m:
        print("YES")
    else:
        print("NO")