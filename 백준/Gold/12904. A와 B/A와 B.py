import sys
t = list(sys.stdin.readline().rstrip())
s = list(sys.stdin.readline().rstrip())

while True:
    if t == s:
        print(1)
        break
    if len(t) > len(s):
        print(0)
        break
    if s[-1] == 'A':
        s.pop()
    elif s[-1] == 'B':
        s.pop()
        s.reverse()