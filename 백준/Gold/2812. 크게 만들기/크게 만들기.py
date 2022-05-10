n, k = map(int, input().split())
numbers = list(input())

cnt = k
answer = list()

for num in numbers:
    while len(answer) > 0 and cnt > 0 and answer[-1] < num:
        del answer[-1]
        cnt -= 1
    answer.append(num)
    
print(''.join(answer[:n-k]))