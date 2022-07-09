import sys, math
number = sys.stdin.readline().rstrip()
num_arr = [0] * 10
answer = 0
for num in number:
    num_arr[int(num)] += 1
six = math.ceil((num_arr[6] + num_arr[9])/2)
num_arr[6], num_arr[9] = six, six
for idx, count in enumerate(num_arr):
    answer = max(count, answer)
print(answer)