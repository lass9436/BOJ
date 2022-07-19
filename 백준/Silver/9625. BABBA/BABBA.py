import sys
N = int(sys.stdin.readline())
dic = {}
dic['A'] = 1
dic['B'] = 0

for _ in range(N):
    countB = dic['A']
    countA = dic['B']
    countB += dic['B']
    dic['A'] = countA
    dic['B'] = countB
    
print(str(dic['A']) + " " + str(dic['B']))