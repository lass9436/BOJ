parenthesis = input()
stack = list()
count = 0

for i in range(len(parenthesis)):
    if parenthesis[i] == '(':
        stack.append(parenthesis[i])
    else:
        if parenthesis[i-1] == '(':
            stack.pop()
            count += len(stack)
        else:
            stack.pop()
            count += 1
print(count)