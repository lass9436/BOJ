import sys
str1 = sys.stdin.readline().rstrip()
str1 = str1.replace("ZERO", "0")
str1 = str1.replace("ONE", "1")
str1 = str1.replace("TWO", "2")
str1 = str1.replace("THREE", "3")
str1 = str1.replace("FOUR", "4")
str1 = str1.replace("FIVE", "5")
str1 = str1.replace("SIX", "6")
str1 = str1.replace("SEVEN", "7")
str1 = str1.replace("EIGHT", "8")
str1 = str1.replace("NINE", "9")
first = True
left = 0
right = 0
ope = ""
answer = 0
for i in range(len(str1)):
    char = str1[i]
    num = 0
    if char == "+" or char == "-" or char == "x" or char == "/" or char == "=":
        right = i
        try:
            num = int(str1[left:right])
        except:
            print("Madness!")
            exit()
        left = i + 1
        if first:
            first = False
            answer = num
            ope = char
        else:
            if ope == "+":
                answer = answer + num
            elif ope == "-":
                answer = answer - num
            elif ope == "x":
                answer = answer * num
            elif ope == "/":
                answer = int(answer / num)
            ope = char
print(str1)
answer = str(answer)
answer = answer.replace("0", "ZERO")
answer = answer.replace("1", "ONE")
answer = answer.replace("2", "TWO")
answer = answer.replace("3", "THREE")
answer = answer.replace("4", "FOUR")
answer = answer.replace("5", "FIVE")
answer = answer.replace("6", "SIX")
answer = answer.replace("7", "SEVEN")
answer = answer.replace("8", "EIGHT")
answer = answer.replace("9", "NINE")
print(answer)