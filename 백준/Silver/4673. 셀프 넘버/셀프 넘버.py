origin_set = set(range(1, 10001))
not_self_set = set()

for i in range(1, 10001):
    num = i
    for j in str(i):
        num += int(j)
    not_self_set.add(num)
    
self_set = sorted(origin_set - not_self_set)

for i in self_set:
    print(i)