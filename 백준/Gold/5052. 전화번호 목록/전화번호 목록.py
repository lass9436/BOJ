class Node:
    def __init__(self):
        self.value = False
        self.childs = {}

class Trie:
    def __init__(self):
        self.root = Node()
        
    def insert(self, phone_num):
        curNode = self.root
        for num in phone_num:
            if num not in curNode.childs:
                curNode.childs[num] = Node()
            curNode = curNode.childs[num]
            if curNode.value:
                return False
        curNode.value = True
        return True
    
for _ in range(int(input().strip())):
    n = int(input().strip())
    phoneList = [input().strip() for _ in range(n)]
    phoneList.sort()
    trie = Trie()
    tof = True
    for num in phoneList:
        tof = trie.insert(num)
        if not tof:
            break
    if tof:
        print("YES")
    else:
        print("NO")
    