import sys
string = sys.stdin.readline().rstrip()
count = 0
for index, s in enumerate(string):
    if index > 0 and string[index-1] != s:
        count += 1
print((count+1)//2)        