N = int(input())

basic = 666
count = 0

while True:
    if "666" in str(basic):
        count += 1
    if count == N:
        break
    else:
        basic += 1
        
print(basic)