n = int(input());
for i in range(n):
    str = "";
    for j in range(n-(i+1)):
        str += " ";
    for k in range(i+1):
        str += "*";
    print(str);
        