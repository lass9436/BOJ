N = int(input())
a = N//5;
b = 0;
possible = False;
while a >= 0:
    remain = N - a * 5;
    if remain % 3 == 0:
        b = remain // 3;
        possible = True
        break;
    a -= 1
if possible:
    print(a + b)
else:
    print(-1)