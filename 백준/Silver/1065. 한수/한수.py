N = int(input())
answer = 0
for i in range(1, N+1):
    num = 0
    if i <= 99:
        answer += 1
    else:
        nums = list(map(int, str(i)))
        if nums[0] - nums[1] == nums[1] - nums[2]:
            answer += 1
print(answer)